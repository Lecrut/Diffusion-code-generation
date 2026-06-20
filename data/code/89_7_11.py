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
    print(subtract(10.0, 4.5))
    print(multiply(6.0, 7.5))
    try:
        print(divide(8.0, 0.0))
    except ValueError as e:
        print(e)