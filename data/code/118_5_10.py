from typing import Union

def validate_input(a: Union[int, float], b: Union[int, float]) -> None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be either int or float")

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    validate_input(a, b)
    return a * b

if __name__ == '__main__':
    result = multiply(5, 10.5)
    print(result)