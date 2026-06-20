from typing import Union

def validate_numbers(a: Union[int, float], b: Union[int, float]) -> None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be numbers')

def signed_difference(a: Union[int, float], b: Union[int, float]) -> int:
    validate_numbers(a, b)
    return a - b
if __name__ == '__main__':
    result1 = signed_difference(10, 5)
    result2 = signed_difference(-5, 100)
    print(result1)
    print(result2)