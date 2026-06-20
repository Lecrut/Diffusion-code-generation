from typing import Union

def validate_numbers(a: Union[int, float], b: Union[int, float]) -> bool:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be numbers.')
    return True

def divide_numbers(a: Union[int, float], b: Union[int, float]) -> float:
    validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError('Division by zero is not allowed.')
    return a / b

if __name__ == '__main__':
    try:
        result = divide_numbers(10, 2)
        print(result)
    except Exception as e:
        print(e)