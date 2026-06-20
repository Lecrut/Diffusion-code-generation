from typing import Union

def divide_numbers(a: Union[int, float], b: Union[int, float]) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

if __name__ == '__main__':
    result = divide_numbers(10, 2)
    print(result)