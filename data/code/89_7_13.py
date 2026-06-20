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
    print(subtract(10.0, 3.14159265))
    print(multiply(2.718281828, 3.141592653))
    try:
        print(divide(1.0, 0.0))
    except ValueError as e:
        print(e)