def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0.0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == '__main__':
    print(add(2.5, 3.7))
    print(subtract(4.8, 1.2))
    print(multiply(2.0, 3.5))
    try:
        print(divide(6.0, 0.0))
    except ValueError as e:
        print(e)