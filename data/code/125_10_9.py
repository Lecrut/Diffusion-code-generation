from typing import Union

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> Union[int, float]:
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b
if __name__ == '__main__':
    print(add(5, 3))
    print(subtract(5, 3))
    print(multiply(5, 3))
    try:
        print(divide(5, 0))
    except ValueError as e:
        print(e)