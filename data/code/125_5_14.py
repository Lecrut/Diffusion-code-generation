from typing import Union

def validate_numbers(a: Union[int, float], b: Union[int, float]) -> None:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    validate_numbers(a, b)
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    validate_numbers(a, b)
    return a - b

if __name__ == '__main__':
    print(add(5, 3))
    print(subtract(10, 4))