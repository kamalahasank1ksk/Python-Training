A=int(input("Enter A value:"))
B=int(input("Enter B value:"))
operation=input("addition/subtraction/multiplication/division:")
def calculator(A,B):
    if(operation=="+"):
        print(A+B)
    elif(operation=="-"):
        print(A-B)
    elif(operation=="*"):
        print(A*B)
    elif(operation=="/"):
        if (B==0):
            print("invalid number")
        else:
            print(A/B)
    else:
        print("the number is invalid")
calculator(A,B)