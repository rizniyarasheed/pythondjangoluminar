
num=int(input("enter the number :"))
res=0
while(num>0):
    digit=num%10
    res=res+digit**3
    num = num // 10
print("res=",res)
