from typing import Union

def validate_numbers(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('Both inputs must be integers')
    return True

def add(a: int, b: int) -> int:
    if validate_numbers(a, b):
        return a + b

def subtract(a: int, b: int) -> int:
    if validate_numbers(a, b):
        return a - b

def multiply(a: int, b: int) -> int:
    if validate_numbers(a, b):
        return a * b

def divide(a: int, b: int) -> Union[int, float]:
    if validate_numbers(a, b):
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b

if __name__ == '__main__':
    print(add(5, 3))
    print(subtract(10, 4))
    print(multiply(7, 2))
    try:
        print(divide(9, 0))
    except ValueError as e:
        print(e)