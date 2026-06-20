def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

if __name__ == '__main__':
    print(add(2.5, 3.7))
    print(subtract(5.1, 2.8))
    print(multiply(4.2, 3.6))
    try:
        print(divide(9.0, 0.0))
    except ValueError as e:
        print(e)