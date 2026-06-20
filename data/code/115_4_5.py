from typing import Union

def validate_inputs(a: Union[int, float], b: Union[int, float]) -> bool:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both inputs must be numbers.')
    if b == 0:
        raise ValueError('Division by zero is not allowed.')
    return True

def divide_numbers(a: Union[int, float], b: Union[int, float]) -> float:
    validate_inputs(a, b)
    return a / b

if __name__ == '__main__':
    try:
        result = divide_numbers(10, 2)
        print(result)
        result = divide_numbers(5.5, 3)
        print(result)
        result = divide_numbers(10, 0)
    except Exception as e:
        print(e)