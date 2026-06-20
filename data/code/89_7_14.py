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
    print(add(1.23456789, 9.87654321))
    print(subtract(10, 3.14159))
    print(multiply(2.71828, 3.14159))
    try:
        print(divide(10, 0))
    except ValueError as e:
        print(e)