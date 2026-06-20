from typing import Union

def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Union[float, str]:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return 'Error: Both inputs must be numbers.'
    if b == 0:
        return 'Error: Division by zero is not allowed.'
    result = a / b
    return result

if __name__ == '__main__':
    dividend = 15.0
    divisor = 3
    outcome = divide_numbers(dividend, divisor)
    print(outcome)