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
    num1 = 10
    num2 = 5

    print(f"Addition of {num1} and {num2}: {add(num1, num2)}")
    print(f"Subtraction of {num1} and {num2}: {subtract(num1, num2)}")
    print(f"Multiplication of {num1} and {num2}: {multiply(num1, num2)}")
    print(f"Division of {num1} by {num2}: {divide(num1, num2)}")