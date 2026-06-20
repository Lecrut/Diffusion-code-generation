from typing import Union

def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Union[float, str]:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return 'Error: Both inputs must be numbers.'
    if b == 0:
        return 'Error: Division by zero is not allowed.'
    return a / b

if __name__ == '__main__':
    result = divide_numbers(15.0, 3)
    print(result)