from typing import Union

def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Union[float, str]:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return 'Error: Both arguments must be numbers.'
    if b == 0:
        return 'Error: Division by zero is not allowed.'
    return a / b
if __name__ == '__main__':
    print(divide_numbers(10, 2))
    print(divide_numbers(7, 3))
    print(divide_numbers('a', 2))
    print(divide_numbers(10, 0))