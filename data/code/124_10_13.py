NUM1 = 10
NUM2 = 5

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
    print(f"Number 1: {NUM1}")
    print(f"Number 2: {NUM2}")
    print(f"Sum: {add(NUM1, NUM2)}")
    print(f"Difference: {subtract(NUM1, NUM2)}")
    print(f"Product: {multiply(NUM1, NUM2)}")
    try:
        print(f"Quotient: {divide(NUM1, NUM2)}")
    except ValueError as e:
        print(e)