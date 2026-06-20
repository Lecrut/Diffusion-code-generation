from typing import Union
DIVISION_BY_ZERO_ERROR = 'Cannot divide by zero'

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> Union[int, float]:
    if b == 0:
        raise ValueError(DIVISION_BY_ZERO_ERROR)
    return a / b
if __name__ == '__main__':
    print(add(5, 3))
    print(subtract(10, 4))
    print(multiply(7, 2))
    try:
        print(divide(9, 0))
    except ValueError as e:
        print(e)