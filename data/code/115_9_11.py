import math

def validate_divisor(divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")

def divide_and_round(dividend, divisor, decimal_places):
    validate_divisor(divisor)
    result = dividend / divisor
    return round(result, decimal_places)

if __name__ == '__main__':
    dividend_large = 12345678901234567890
    divisor_small = 12345
    decimal_places = 5
    result = divide_and_round(dividend_large, divisor_small, decimal_places)
    print(result)