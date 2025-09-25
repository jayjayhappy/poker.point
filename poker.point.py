import math
def tran(a):
    if a=='J':
        return 0.5
    if a=='Q':
        return 0.5
    if a=='K':
        return 0.5
    elif a=='A':
        return 1
    else:
        return int(a)
    
x=tran(input())+tran(input())+tran(input())
y=tran(input())+tran(input())+tran(input())

if x>10.5:
    x=0
if y>10.5:
    y=0
if float(x)==int(x):
    x=int(x)
if float(y)==int(y):
    y=int(y)
print(x)
print(y)
if x>y:
    print("X Win")
elif x<y:
    print("Y Win")
else:
    print("Tie")
