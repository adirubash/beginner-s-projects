from turtle import *
from calendar import isleap

a = numinput("age calculator","please type your birth year")
result = 2024-a
result2 = result/4
print("age:",result)
print("age in months:",result*12)
def leap_year(a):
    if isleap(a):
        print("leap year age in days:",result*365+result2)
    else:
        print("not leap year age in days:",result*365)

leap_year(a)