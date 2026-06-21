def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == '__main__':
    sample_values = [10, 5]
    print("Addition:", add(sample_values[0], sample_values[1]))
    print("Subtraction:", subtract(sample_values[0], sample_values[1]))
    print("Multiplication:", multiply(sample_values[0], sample_values[1]))
    try:
        print("Division:", divide(sample_values[0], sample_values[1]))
    except ValueError as e:
        print(e)