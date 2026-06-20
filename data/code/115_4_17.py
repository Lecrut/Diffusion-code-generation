from typing import Union

def divide_numbers(num1: Union[int, float], num2: Union[int, float]) -> Union[float, str]:
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return 'Error: Both inputs must be numbers.'
    if num2 == 0:
        return 'Error: Division by zero is not allowed.'
    return num1 / num2
if __name__ == '__main__':
    result = divide_numbers(10, 2)
    print(result)