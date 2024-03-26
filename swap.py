list=[1,2,3,4,5,6,7,8,9,10]
print(list)
t=list[0]
list[0]=list[-1]
list[-1]=t
print(list)