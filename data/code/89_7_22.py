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
    print(add(2.5, 3.7))
    print(subtract(4.8, 1.9))
    print(multiply(6.2, 3.4))
    try:
        print(divide(10.0, 0.0))
    except ValueError as e:
        print(e)