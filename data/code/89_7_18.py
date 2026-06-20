EPSILON = 1e-09

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if abs(b) < EPSILON:
        raise ValueError('Cannot divide by zero or near-zero value')
    return a / b
if __name__ == '__main__':
    print(add(1.1, 2.2))
    print(subtract(3.3, 1.1))
    print(multiply(4.4, 5.5))
    try:
        print(divide(6.6, 0))
    except ValueError as e:
        print(e)