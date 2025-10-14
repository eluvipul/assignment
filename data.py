#1 Program to find the greatest of 3 ages
def greatestData(n1,n2,n3):
    result = n1 if(n1>n2 and n1>n3) else(n2 if (n2>n3) else n3)
    print(f"greatest of ages is: {result}")
x=int(input("Enter age1:"))
y=int(input("Enter age2:"))
z=int(input("Enter age3:"))
greatestData(x,y,z)

#2 Program to find the sum of digits of a 3 digit number

def sum_digits(n1):
    n2=n1%10
    n3=n1/10
    n4=n3%10
    n5=n3/10
    s=int(n4+n2+n5)
    print(f"The sum is: {s}")
x1=int(input("Enter a 3 digit number"))
sum_digits(x1)

#3 Program to convert to farenheit

def ctof(c):
    res=int(c*1.8+32)
    print(f"Temperature in Farenheit is:{res}")
c=int(input("Enter temperature in celsius"))
ctof(c)

#4 Program to swap 2 numbers

def swap_numbers(a,b):
    print(f"The numbers before swapping: a=",a,"b=",b)
    a,b=b,a
    print("After swapping : a=",a,"b=",b)
a=50
b=40

swap_numbers(a,b)

#5 Program to reverse a number

def rev_num(n):
    rn=0
    while n!=0:
        r=n%10
        rn=rn*10+r
        n=n//10
    print(f"The reversed number is {rn}")
x=int(input("Enter a number"))
rev_num(x)


#6 Program to find a number is odd or even

def odd_even(n):
    if n%2==0:
        print(f"the number is even")
    else:
        print(f"the number is odd")

a=int(input("Enter the number"))
odd_even(a)

#7 Program to find a given year is leap year or not

def leap_year(n):
    if(n%4==0 and n%100!=0) or ( n%400==0):
        print(f"The year is a leap year")
    else:
        print(F"the year is not a leap year")
b=int(input("Enter the year"))
leap_year(b)

#8 Program to find the euclidean distance between 2 coordinates

import math
from math import pow
from math import sqrt

def eu_dist(x1,y1,x2,y2):
    d=0
    p1=x2-x1
    p2=y2-y1
    print(p1)
    print()
    print(p2)
    s1=pow(p1,2)
    print()
    print(s1)
    s2=pow(p2,2)
    print(s2)
    s=s1+s2
    print(s)
    d=sqrt(s)
    print(f"the distance is:{d}")
a=int(input("Enter the x1 cordinate"))
b=int(input("enter y1 coordinate"))
c=int(input("enter x2 coordinate"))
d=int(input("enter y2 coordiante"))
eu_dist(a,b,c,d)

#9 Program to find the given angles form a triangle or not

def tri(a,b,c):
    d=a+b+c
    if d==180:
        print(f"The angles form a triangle")
    else:
        print(f"This does not form a triangle")
x=int(input("Enter first angle"))
y=int(input("Enter second angle"))
z=int(input("Enter third angle"))
tri(x,y,z)

#10 Program to find the profit and loss

def profit_loss(sp,cp):
    if(sp>cp):
        p=sp-cp
        print("The profit is ",p)
    else:
        l=cp-sp
        print(f"The loss is ",l)
a=int(input("Enter selling price "))
b=int(input("Enter cost price "))
profit_loss(a,b)

    






          

