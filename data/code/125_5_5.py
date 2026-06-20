from typing import Union

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

if __name__ == '__main__':
    result_add = add(5, 3)
    result_sub = subtract(10, 4)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_sub}")