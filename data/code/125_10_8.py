from typing import Tuple

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> Tuple[int, str]:
    if b == 0:
        return 0, "Cannot divide by zero"
    return a // b, ""

if __name__ == '__main__':
    result_add = add(5, 3)
    result_subtract = subtract(10, 4)
    result_multiply = multiply(7, 2)
    result_divide, error_message = divide(9, 0)

    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_subtract}")
    print(f"Multiplication: {result_multiply}")
    print(f"Division: {result_divide} (Error: {error_message})")