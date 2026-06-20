from typing import Union

def validate_input(a: Union[int, float], b: Union[int, float]) -> bool:
    return isinstance(a, (int, float)) and isinstance(b, (int, float))

def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if not validate_input(a, b):
        raise ValueError("Both arguments must be numbers (int or float).")
    return a + b

if __name__ == '__main__':
    print(add_numbers(3, 5))
    print(add_numbers(2.5, 4.7))