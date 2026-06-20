from typing import Union

def validate_numbers(a: Union[int, float], b: Union[int, float]) -> None:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    validate_numbers(a, b)
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    validate_numbers(a, b)
    return a - b

if __name__ == '__main__':
    result_add = add(5, 3)
    result_sub = subtract(10, 4)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_sub}")