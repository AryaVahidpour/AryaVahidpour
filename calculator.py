#start
print('Welcome to Calculator:)')
wTc = 0
while wTc < 5:
    print("*")
    wTc = wTc+1
#modules
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
#select operations
print("Select operation:")
print("1. Add(+)")
print('or')
print("2. Subtract(-)")
print('or')
print("3. Multiply(x)")
print('or')
print("4. Divide(÷)")
wTc = 0
while wTc < 5:
    print("*")
    wTc = wTc+1
while True:
    choice = input("Enter choice (1 - 2 - 3 - 4): ")
#enter numbers
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError: #error when the user didn't write numbers
            wTc = 0
            while wTc < 5:
                print("*")
                wTc = wTc+1
            print("Error! Please try again.")
            print(' |')
            print(' |')
            print(' |')
            print('\_/')
            continue
        #do operations
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            #error when the user didn't write operations correct
    else:
        print('*')
        print("Error! Please enter one of four operations as these numbers: ('1' or '2' or '3' or '4').")
        print(' |')
        print(' |')
        print(' |')
        print('\_/')