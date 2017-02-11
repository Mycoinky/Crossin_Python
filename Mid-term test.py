# coding:utf-8
#!/usr/bin/env python

f = file('report.txt')        #打开读取文件
data = f.readlines()
f.close()
#print data

Total_stu = [] #用于统计主数列
Aver_stu = [] # 用于统计列的平均数

for line in data:
    each_stu = line.split()  #拆分数列，使其变得可加
#    print each_stu
    num = len(each_stu) - 1
    ieach_stu = each_stu[1:]
    ieach_stu = map(int, ieach_stu)   #转化成整数，使其变得可加
    total = sum(ieach_stu)
    aver = round(float(total)/num,1)                 #平均数保留一位小数

    Aver_stu.append(ieach_stu)       #形成一个 新的只有分数的list的list

    n=1                             #用于索引替换Fail
    for score in each_stu[1:]:
        if int(score) < 60:
            each_stu[n] = 'Fail'
        n = n+1
    each_stu.append(total)
    each_stu.append(aver)
    Total_stu.append(each_stu)

def f(x):             #Map函数的参数
    return round(float(x)/30,1)   #保留一位小数

print Aver_stu         #输出测试
Average = map(sum,zip(*Aver_stu))
Final_aver = map(f,Average)

total_aver = sum(Final_aver)  #计算平均数的总数与平均数
num = len(Final_aver)
aver_aver = round(float(total)/num,1)   #计算平均数的总数与平均数，保留一位小数

print '####################'  # Append头和尾部数据
Final_aver.insert(0,'平均')
Final_aver.insert(0,31)
Final_aver.append(total_aver)
Final_aver.append(aver_aver)
print Final_aver
print '####################'

#下列函数可以直接排序，按照list其中一列排序
Total_stu = sorted(Total_stu, key=lambda Total_stu_tuples: Total_stu_tuples[10],reverse=True)
#print Total_stu

i=1
Final_Num = []
for jeach_stu in Total_stu:
#    print jeach_stu
    jeach_stu.insert(0, i)
    Final_Num.append(jeach_stu)
    i = i+1

First_line = [['名次',"姓名","语文",'数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']]
First_line.extend(Total_stu)
First_line.extend([Final_aver])  #把平均数加入list
print First_line

ff = open('report_modified.txt'.decode('utf-8'), 'w')

for i in First_line:
    for j in i:
        ff.write(str(j).center(7,' '))
    ff.write("\n")

ff.close()






