from typing import Union

def validate_inputs(a: Union[int, float], b: Union[int, float]) -> None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")

def signed_difference(a: Union[int, float], b: Union[int, float]) -> int:
    validate_inputs(a, b)
    return a - b

if __name__ == '__main__':
    print(signed_difference(10, 5))
    print(signed_difference(-5, 100))
    print(signed_difference(3.14, 1.618))