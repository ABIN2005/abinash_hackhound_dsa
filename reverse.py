num=int(input("enter the number"))
rev=0
rem=0
while num>0:
    rem=num%10
    num=num//10
    rev=rev*10+rem
print("the reverse of a number is",rev)
    
