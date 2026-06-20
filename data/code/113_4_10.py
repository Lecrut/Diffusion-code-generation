from typing import Union

def validate_numbers(a: Union[int, float], b: Union[int, float]) -> None:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers.")

def subtract_values(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    validate_numbers(a, b)
    return a - b

if __name__ == '__main__':
    result = subtract_values(10, 5)
    print(result)