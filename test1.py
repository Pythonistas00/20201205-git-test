# 20201205 18:59 add this annotation in testing branch
import os
def text_GeneAndExtr(images_Path, Path):
    train_Path = images_Path + "\\train.txt"
    test_Path = images_Path + "\\test.txt"
    images_list = os.listdir(images_Path + "\images")
    
    with open(train_Path, 'w') as f:
        for i in images_list:
            f.write('/usr/src/app/preTrain_input/' + Path + '/images' + i)
            f.write('\n')

    extract1 = []
    with open(train_Path, 'r') as f1:
        for line in f1.readlines():
            line = line.strip('\n') #去掉列表中每一个元素的换行符
            extract1.append(line) # 读取txt中的字符串生成列表

    with open(test_Path, 'w') as ff1:
        for i in extract1[::5]:
            ff1.write(i)
            ff1.write('\n')

    # 删除
    del extract1[::5]
    
    with open(train_Path, 'w') as ff2:
        for i in extract1:
            ff2.write(i)
            ff2.write('\n')


    f.close()
    ff1.close()
    ff2.close()

if __name__ == "  main  ":
    images_Path = r"D:\Projects"
    Path = "pokemon"
    text_GeneAndExtr(images_Path, Path)
