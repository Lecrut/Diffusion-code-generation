def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == '__main__':
    num1 = 23.4
    num2 = 5.6
    print(f"Addition: {add(num1, num2)}")
    print(f"Subtraction: {subtract(num1, num2)}")
    print(f"Multiplication: {multiply(num1, num2)}")
    try:
        print(f"Division: {divide(num1, num2)}")
    except ValueError as e:
        print(e)