from typing import Union

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    sum_result = add(num1, num2)
    diff_result = subtract(num1, num2)
    print(f"Addition: {sum_result}")
    print(f"Subtraction: {diff_result}")