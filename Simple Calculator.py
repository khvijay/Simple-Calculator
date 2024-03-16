def add(a, b):
    return a + b

def Substract(a, b):
    return a - b

def Multiply(a, b):
    return a * b

def Divide(a, b):
    return a / b

def add(a, b):
    if b == 0:
        return "Error: division by zero!"
    return a / b

num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))

print("1. Addition", "2. Subtrsction", "3. Multiply", "4. Divide")
# print("2. Subtrsction ")
# print("3. Multiply" )
# print("4. divide ")
choice = int(input("enter your choice (1/2/3/4)5 "))

if choice == 1:
    print("result:", add(num1, num2))
elif choice == 2:
    print("result:", Substract(num1, num2))
elif choice == 3:
    print("result:", Multiply(num1, num2))
elif choice == 4:
    print("result:", Divide(num1, num2))
else:
    print("invalid input")