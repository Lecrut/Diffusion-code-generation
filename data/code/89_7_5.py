def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

if __name__ == '__main__':
    a = 10.5
    b = 3.2
    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    try:
        print(f"Division: {divide(a, b)}")
    except ValueError as e:
        print(e)