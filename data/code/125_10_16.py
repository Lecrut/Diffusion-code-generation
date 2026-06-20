from typing import Union

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: float, b: float) -> Union[float, str]:
    if b == 0:
        return 'Division by zero'
    return a / b
if __name__ == '__main__':
    print(add(5, 3))
    print(subtract(10, 4))
    print(multiply(7, 2))
    print(divide(9, 3))
    print(divide(5, 0))