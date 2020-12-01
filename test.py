#!/usr/bin/python3
# -*- coding: UTF-8 -*-


#入门级实例：
#一定要确保代码的四空格缩进
#运行命令,指定文件名称： python test.py
#查询版本：python --version
#查询所有的库：pydoc modules
#查询库的用法，如查询shutil库的用法：pydoc shutil

#第一个实例
print("Hello world!")
# 输出结果：
# Hello world!

#支持中文，注意文件头加了coding: UTF-8
print("您好，世界!")
# 输出结果：
# 您好，世界!


#字符操作
strA = "abc"
strB = "efg"
print("strA + strB=", strA + strB)  #合并字符
print("hello %s" % strA)            #格式化字符，使用%连接
print("strA * 2 =", strA * 2)       #重复输出字符串
print("a[1] =", strA[1])            #通过索引获取字符串中字符
print("a[2:3] =", strA[2:3])        #截取字符串中的一部分
if("b" in strA):                    #in:包含给定的字符
    print("b在变量strA中")
if("d" not in strA):                #not in:不包含字符
    print("d不在变量strA中")
#输出结果：
# ('strA + strB=', 'abcefg')
# hello abc
# ('strA * 2 =', 'abcabc')
# ('a[1] =', 'b')
# ('a[2:3] =', 'c')
# b在变量strA中
# d不在变量strA中


# 数组的使用
# 列表索引从 0 开始, 添加元素使用append, 删除元素使用del, 统计个数使用len
listData = ['red', 'green', 'blue', 'yellow']
listData.append("white")
listData.append("Black")
del listData[2]   #删除第3个元素，blue
print("listData first=%s" %listData[0] )
print("listData len=%s" % len(listData));
print("listData = ", listData)
#判断是否在列表中
for item in listData:   
    if(item == "green"):
        print("green is in listData")
#或使用更简单的判断
if("red" in listData):
    print("red is in listData")
# 输出结果：
# listData first=red
# listData len=5
# ('listData = ', ['red', 'green', 'yellow', 'white', 'Black'])
# green is in listData
# red is in listData


# 元组: 不允许修改值
array = ('Google', 'Runoob', 1997, 2000)
print ("array[0]: ", array[0])
# 输出结果：
# ('array[0]: ', 'Google')


# 字典
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中
dicts = {'Name':'zzz', 'Age':8, 'Class':'One'}
print ("dicts['Name']: ", dicts['Name'])
print ("dicts['Age']: ", dicts['Age'])
# 输出结果
# ("dicts['Name']: ", 'zzz')
# ("dicts['Age']: ", 8)


# 字典数组的使用，例子：查找指定主题的配置
Themes_Config = [
    {'name': '默认', 'fgcolor': '#000000', 'bgcolor': '#FFFFFF'},
    {'name': '护眼模式', 'fgcolor': '#000000', 'bgcolor': '#CCE8CF'},
    {'name': '夜间模式', 'bgcolor': '#FFFFFF', 'bgcolor': '#000000'},
]
selectName = '护眼模式'
selectTheme = None
for item in Themes_Config:
    name = item['name']
    if name:
        if selectName.decode('utf-8') == name.decode('utf-8'):  # 中文字需要解析
            selectTheme = item
            break
print("selectTheme=", selectTheme)
# 输出结果
# ('selectTheme=', {'bgcolor': '#CCE8CF', 'name': '\xe6\x8a\xa4\xe7\x9c\xbc\xe6\xa8\xa1\xe5\xbc\x8f', 'fgcolor': '#000000'})

#条件判断：if-else
flag = False
if flag == True:
    print("check flag true")
else:
    print("check flag false")
# 输出结果：
# check flag false

# 条件判断2: if-elif-else
state = 2
if state == 1:
    print("check state 1")
elif state == 2:
    print("check state 2")
else:
    print("check state 3")
#输出结果：
# check state 2


#条件判断3：与或的使用
num = 7
# 判断值是否在0~6或者12~20之间
if (num >= 0 and num <= 6) or (num >= 12 and num <= 20):    
    print 'num in range'
else:
    print 'num not in range'
# 输出结果: 
# num not in range

# 循环语句
loop = 1
while loop < 10:
    if loop == 5:
        break
    print("test while loop=%s"%loop)
    loop += 1
#输出结果：
# test while loop=1
# test while loop=2
# test while loop=3
# test while loop=4

# 循环语句2
forlist = ["apple", "pear", "banana"]
for item in forlist:
    print("当前水果: %s"%item)
#输出结果：
# 当前水果: apple
# 当前水果: pear
# 当前水果: banana

# 循环语句3--通过序列索引
forlist2 = ["apple1", "pear2", "banana3"]
for index in xrange(len(forlist2)):
    print("当前水果序列: %s"%forlist2[index])
#输出结果
# 当前水果序列: apple1
# 当前水果序列: pear2
# 当前水果序列: banana3


#测试输入数字raw_input,转化数字，结果+10，循环3次
TestInput = False   #测试输出开关
if(TestInput):
    inputCount = 1
    while inputCount <= 3:
        strInput = raw_input("请输入数字：")
        inputCount += 1;

        if not (strInput is None) and len(strInput) > 0:
            intputData = int(strInput);
            intputData += 10;
            print("out:%s"%intputData)
    print("out:End")
#输出：
# 请输入数字：5
# out:15
# 请输入数字：6
# out:16
# 请输入数字：7
# out:17
# out:End



#测试函数
def funcAddData(bbb):
    return bbb + " Test"

print(funcAddData("myFunc"))
#输出：myFunc Test

#匿名函数
addFunc = lambda arg1, arg2: arg1+arg2
print("func2: addData=%s"%addFunc("aaa", "bbb"))
#输出：func2: addData=aaabbb

#区分全局变量和局部变量
total = 0 # 这是一个全局变量
def sum( arg1, arg2 ):
   total = arg1 + arg2 # total在这里是局部变量.
   print "函数内是局部变量 : ", total
   return total
#调用sum函数
sum( 10, 20 )
print "函数外是全局变量 : ", total
#输出结果(不能改变全局变量的值)：
# 函数内是局部变量 :  30
# 函数外是全局变量 :  0


#引用全局变量
total = 0 # 这是一个全局变量
def sum_global( arg1, arg2 ):
    global total           #声明引用全局变量，并修改全局变量的值
    total = arg1 + arg2 
    print "函数内变量total : ", total
    return total
#调用sum函数
sum_global( 10, 20 )
print "函数外变量total : ", total
# 函数内变量total :  30
# 函数外变量total :  30



#------------------------------------------------------------------
#实例1：复制文件，注：需要准备一张 "1.png"图片到当前目录，测试复制命令

#复制文件
import shutil
import os

TestCopy2 = False   #测试开关

if(TestCopy2):
    try:
        # 复制
        shutil.copy("1.png", "2.png")
        # 判断是否复制成功
        if(os.path.isfile("2.png")):
            print("shutil copy success")
    except IOError as e:
       print("Unable to copy file. %s" % e)
    except:
       print("Unexpected error:", sys.exc_info())



#删除目录，使用shutil.rmtree
import shutil
TestRemove2 = False
if(TestRemove2):
    curDir = os.getcwd()       #获取当前目录
    subDir = curDir + "/2"
    print("subDir=", subDir)
    try:
        shutil.rmtree(subDir, True)
    except IOError as e:
       print("Unable to shutil.rmtree file. %s" % e)
    except:
       print("Unexpected shutil.rmtree error:", sys.exc_info())    



#测试移动文件，使用shutil.move，建立函数
def moveFile(srcFile, destFile):
    if(len(srcFile) == 0 or len(destFile) ==  0):
        print("move file parms none")
        return

    if not os.path.isfile(srcFile):
        print("not exit file = %s" % srcFile)
    else:
        #分离路径目录和文件名
        fpath, fname = os.path.split(destFile)

        #不存在目录则创建
        if not os.path.exists(fpath):
            os.makedirs(fpath)

        #移动文件
        shutil.move(srcFile, destFile)

        #判断是否移动成功
        if os.path.isfile(destFile):
            print("moveFile success: %s" % destFile)


#测试复制文件，使用shutil.copyfile，建立函数
def copyFile(srcFile, destFile):
    print("copyFile: srcFile=", srcFile)
    print("copyFile: destFile=", destFile)

    if(len(srcFile) == 0 or len(destFile) ==  0):
        print("copyFile file parms none")
        return
    if not os.path.isfile(srcFile):
        print("not exit file = %s" % srcFile)
    else:
        #分离路径目录和文件名
        fpath, fname = os.path.split(destFile)

        #不存在目录则创建
        if not os.path.exists(fpath):
            os.makedirs(fpath)

        #复制文件
        shutil.copyfile(srcFile, destFile)     

        #判断是否移动成功
        if os.path.isfile(destFile):
            print("Test copyFile success: %s" % destFile)

TestCopyFile = True
if TestCopyFile:
    copyFile("./1.png", "./2.png")
    #moveFile("./1.png", "./img/2.png")
    

#------------------------------------------------------------------
#实例2：测试读写
#注：需要手动创建file1.txt，添加几行字符内容

#读文件，逐行读入
def readFile():
    fd = None
    try:
        fd = open("file1.txt", "r");
        while(True):
            line = fd.readline();
            if(len(line) == 0):
                break;
            line = line.replace("\n", "")
            print("line = %s" % line)
    except Exception as e:
        print("Unable readFile %s" % e)
    finally:
        if(fd):
            print("close file")
            fd.close();

# 一次读入内存，文件大时会占内存
def readFileLines():
    fd = None
    try:
        fd = open("file1.txt", "r");
        lines = fd.readlines();

        for item in lines:
            item = item.replace("\n", "")
            print("line item = %s" % item)
    except Exception as e:
        print("Unable readFile2 %s" % e)
    finally:
        if(fd):
            print("close file")
            fd.close();

#写入文件，使和with避免频繁使用 try-finally
def readAndWriteFile():
    lines = None
    with open("file1.txt", "r") as fd:
        lines = fd.readlines()
        fd.close();

    if(lines):
        with open("file2.txt", "w") as wd:
            if(wd):
                for one in lines:
                    wd.write(one)
                wd.close();


# 注：需要准备一个 "file1.txt"到当前目录，输入若干内容
TestFile = True
if(TestFile):
    # readFile()
    # readFileLines();
    readAndWriteFile()

#------------------------------------------------------------------
#实例3：打印当前目录下的所有文件和目录（遍历所有），  注：需要准备一些文件和目录

import os
def fileDirName(fileDir):
    for root, dirs, file in os.walk(fileDir):
        print("root=%s"%root)
        print("dirs=%s"%dirs)
        print("file=%s"%file)

TestDir = False   #测试开关
if(TestDir == True):
    #获取当前路径
    fileDir = os.getcwd()       #获取当前目录
    print("fileDir=%s"%fileDir)
    fileDirName(fileDir);



#------------------------------------------------------------------
#实例4：保留指定目录下指定的文件
#思想：
import os
#删除文件
def removeFile(path):
    if(path):
        os.remove(path)
        if(not os.path.isfile(path)):
            print("removeFile: %s" % path)

#删除目录
def removeDir(path):
    if(path):
        print("removeDir: path=%s" % path)
        try:
            shutil.rmtree(path, True)
        except IOError as e:
           print("Unable to removeDir file. %s" % e)

#删除所有空目录
def removeEnptyDir(path):
    if(path):
        for root, dirs, files in os.walk(path):
            if(len(dirs) == 0 and len(files) == 0):
                removeDir(root)

#清除文件列表
def removeFileList(curDir, allList):
    outList = []
    if ((len(curDir) > 0) and (len(allList) > 0)):
        #注意files是数组，表示当前目录下所有的文件名称，root是当前目录路径，dirs表示当前目录下的子目录名称（数组）
        for root, dirs, files in os.walk(curDir):
            # print("root=%s"%root)
            # print("dirs=%s"%dirs)
            # print("files=%s"%files)
            
            for fileName in files:
                isInclude = False;

                #是否包括在allList列表中
                for item in allList:
                    if(item in fileName):
                        isInclude = True
                        break

                filePath = root + "/" + fileName

                #不包括删除，否则输出该文件路径
                if(not isInclude):
                    removeFile(filePath)
                else:
                    outList.append(filePath)
    return outList;


#清除资源文件（清除当前目录下的res目录，清除名单不包括文件列表名称[见配置fileList]）
def clearRes():
    #配置要清除的目录
    filePath = "/res"

    #配置要保留的文件名称
    fileList = [
        "ComRes.png",
        "GameBase.png",
    ]
    
    #获取当前目录
    curDir = os.getcwd()       
    curDir = curDir + filePath

    #清除不包括的文件
    outList = removeFileList(curDir, fileList)

    #清除空目录
    removeEnptyDir(curDir);

    #输出保留的文件列表
    print("-----------------------")
    for item in outList:
        print("out = %s" % item)

#执行清除文件
TestClear = False;
if(TestClear):
    clearRes();

print("----------------------- All end ----------------------- ")











