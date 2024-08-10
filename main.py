def sum():
    return a+b
def minus():
    return a-b
def multiply():
    return a*b
def divide():
    return a/b
def squre():
    return a**b
def modlus():
    return a%b
def operatorcheck(a,b):
    # operator=input("select any arithematic operator to perform the operation:\n")
    # if operator=="+":
    print(f"the sum is {sum()}")
    # if operator=="-":
    print(f"the minus of both number is {minus()}")
    # if operator=="*":
    print(f"the multiplication of both number give us {multiply()}")
    # if operator=="/":
    print(f"the division  of both number give us  {divide()}")
    print(f"the modlus of a to b is {modlus()}")
    print(f"the exponentiation of {a} to {b}  is :  {squre()}")
a=int(input("enter first number here:\n"))
# operator=input('''select any arithematic operator to perform the operation:''')
b=int(input("enter your second here:\n"))
operatorcheck(a,b)