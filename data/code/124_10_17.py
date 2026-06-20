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
    num1 = 8
    num2 = 4
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Sum: {add(num1, num2)}")
    print(f"Difference: {subtract(num1, num2)}")
    print(f"Product: {multiply(num1, num2)}")
    try:
        print(f"Quotient: {divide(num1, num2)}")
    except ValueError as e:
        print(e)