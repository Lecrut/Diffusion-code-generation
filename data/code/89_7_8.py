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
    print(add(1.1, 2.2))
    print(subtract(5.5, 3.3))
    print(multiply(4.4, 2.5))
    try:
        print(divide(7.0, 0))
    except ValueError as e:
        print(e)