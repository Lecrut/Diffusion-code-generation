def validate_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers")

def add(a, b):
    validate_numbers(a, b)
    return a + b

def subtract(a, b):
    validate_numbers(a, b)
    return a - b

def multiply(a, b):
    validate_numbers(a, b)
    return a * b

def divide(a, b):
    validate_numbers(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == '__main__':
    num1 = 10.5
    num2 = 3.2
    print(f"Addition: {add(num1, num2)}")
    print(f"Subtraction: {subtract(num1, num2)}")
    print(f"Multiplication: {multiply(num1, num2)}")
    try:
        print(f"Division: {divide(num1, num2)}")
    except ValueError as e:
        print(e)