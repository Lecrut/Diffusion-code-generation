def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b
if __name__ == '__main__':
    print(add(5, 3))
    print(subtract(10, 4))
    print(multiply(7, 2))
    try:
        print(divide(9, 0))
    except ValueError as e:
        print(e)