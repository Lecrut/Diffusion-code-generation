def perform_calculations():
    a = 20
    b = 5
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division:", "Error: Cannot divide by zero")
if __name__ == '__main__':
    perform_calculations()