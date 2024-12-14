# calculator
import math

adlst=[]
sublst=[]
mullst=[]
divlst=[]

def ad():
    sum=0
    n=int(input('Enter no.:'))
    adlst.append(n)
    a=input('Do you want to add more no.: (y/n) ')
    if a=='y' or a=='Y':
        ad()
    else:
        for i in adlst:
            sum+=i
    print(sum)

def sub():
    sub=0
    n=int(input('Enter no.:'))
    adlst.append(n)
    a=input('Do you want to add more no.: (y/n) ')
    if a=='y' or a=='Y':
        sub()
    else:
        for i in sublst:
            sub-=i
    print(sub)

def mul():
    mul=0
    n=int(input('Enter no.:'))
    mullst.append(n)
    a=input('Do you want to add more no.: (y/n) ')
    if a=='y' or a=='Y':
        mul()
    else:
        for i in mullst:
            mul*=i
    print(mul)

def div():
    div=0
    n=int(input('Enter no.:'))
    divlst.append(n)
    a=input('Do you want to add more no.: (y/n) ')
    if a=='y' or a=='Y':
        div()
    else:
        for i in sublst:
            div-=i
    print(div)

def main():
    try:
        print('Welcome to Calculator')
        print('''Enter:
            1 - Add
            2 - Subract
            3 - Multiply
            4 - Divide''')
        ans=int(input('>>'))
        if ans==1:
            ad()
        elif ans==2:
            sub()
        elif ans==3:
            mul()
        elif ans==4:
            div()
        else:
            print('Invalid option!')
            main()
        
    except:
        print('Retry!')

main()