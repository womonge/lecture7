import math

def introduction_message():
    print("This program computes the roots")
    print("of a second order equaition:")
    print()
    print("    ax^2 + bx + c = 0    ")
    print()


def input_and_solve():

    a=eval(input("please enter a:"))
    b=eval(input("please enter b:"))
    c=eval(input("please enter c:"))

    delta=(b*b)-(4*a*c)
    x1=-b + math.sqrt(delta)     
    x2=-b - math.sqrt(delta)

    print()
    print("The roots are:")
    print("x1=",x1)
    print("x2=",x2)

def final_message():

    print()
    print("Thank you for using this program")
    print("================================")
    print("***   All rights reserved    ***")
    print("================================")
    print()

introduction_message()
input_and_solve()
final_message()
           
