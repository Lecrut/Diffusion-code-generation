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
    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))
    try:
        print("Division:", divide(a, b))
    except ValueError as e:
        print(e)