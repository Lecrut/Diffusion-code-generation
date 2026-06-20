from typing import Union

def validate_numbers(a: Union[int, float], b: Union[int, float]) -> bool:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be numbers.')
    if b == 0:
        raise ZeroDivisionError('Division by zero is not allowed.')

def divide_numbers(a: Union[int, float], b: Union[int, float]) -> float:
    validate_numbers(a, b)
    return a / b

if __name__ == '__main__':
    result = divide_numbers(10, 2)
    print(result)