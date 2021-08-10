list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list.append(ele)
print(list)
for ele in list:
    if(ele>0):
        print(ele, end = " ")
