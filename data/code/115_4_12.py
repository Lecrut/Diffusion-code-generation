from typing import Union

def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Union[float, str]:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return 'Error: Both inputs must be numbers.'
    if b == 0:
        return 'Error: Division by zero is not allowed.'
    quotient = a / b
    return quotient

if __name__ == '__main__':
    sample_dividend = 20.5
    sample_divisor = 4
    division_result = divide_numbers(sample_dividend, sample_divisor)
    print(division_result)