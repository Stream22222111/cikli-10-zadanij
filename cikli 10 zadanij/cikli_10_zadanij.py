﻿print("Задание 2")
A=int(input())
print(sum(range(1,A+1)))
print("Задание 4")
for i in range(10,21):
    print(i,i**2)
print("Задание 12")
n=int(input("введите кол во косилок "))
m=int(input("сколько работала первая косилка "))
tul=0
for i in range(n):
    tul+=m
    m+=1/6
print(f"{tul} tundi kogu meeskond tootas")

print("Задание номер 9")
S=float(input("Введите первоначальную сумму вклада "))
N=float(input("Введите количество лет "))
AB=S*(1+(3/100)/365)**(N*365)
print("результат: "+str(AB))
print("Задание номер 8")
D=float(input("введите количество дюймов"))
F=D*(2+1/2)
print("Результат дюймы в сантиметры "+str(F))
print("Задание 1")
#1. Вводят 15 чисел. Определить, сколько среди них целых. задание 1
x=0
for i in range(1,6,1):
    A=float(input(f" введите A:"))
    int(A)==A
    if int(A)==A: x+=1
print(x)
print("Задание 3")
w=1
for i in range(1,8,1):
    A=float(input(f"введите A:"))
    if A>0:
        if int(A)==A: w*=A
print(round(w),)
print("Задание 5")
j=0
for i in range(1,6,1):
    N=float(input(f"Введите N:"))
    if N<0:
        if int(N)==N: j+=N
print(round(j),)
print("Задание 6")
z, p, n, counter=0,0,0,0

print("sisestage 5 num")
while counter<5:
    counter+=1
    a=int(input())
    if a>0:
        p+=1
    elif a<0:                  
        n+=1
    else:
        z+=1
print("позитивный",p)
print("негативный",n)
print("нули",z)
print("Задание 7")
for i in range(10,200,10):
    if i%10==0: 
        print(i)
