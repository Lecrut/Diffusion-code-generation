def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b
if __name__ == '__main__':
    sample_values = [(10, 5), (20, 3), (7, 4), (9, 0)]
    for x, y in sample_values:
        try:
            print(f'Addition: {add(x, y)}')
            print(f'Subtraction: {subtract(x, y)}')
            print(f'Multiplication: {multiply(x, y)}')
            print(f'Division: {divide(x, y)}')
        except ValueError as e:
            print(e)