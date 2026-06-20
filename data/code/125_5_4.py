from typing import Union

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    result = a - b
    return result

if __name__ == '__main__':
    operand1 = 20
    operand2 = 7
    sum_result = add(operand1, operand2)
    diff_result = subtract(operand1, operand2)
    print(f"Addition: {sum_result}")
    print(f"Subtraction: {diff_result}")