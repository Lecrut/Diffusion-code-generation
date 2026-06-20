from typing import Union

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

if __name__ == '__main__':
    num1 = 20
    num2 = 8
    result_add = add(num1, num2)
    result_sub = subtract(num1, num2)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_sub}")