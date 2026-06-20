import math

def validate_divisor(divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return divisor

def round_result(dividend, divisor, decimal_places):
    result = dividend / divisor
    return round(result, decimal_places)

def perform_division(dividend, divisor, decimal_places):
    validated_divisor = validate_divisor(divisor)
    return round_result(dividend, validated_divisor, decimal_places)

if __name__ == '__main__':
    dividend_large = 12345678901234567890
    divisor_small = 12345
    decimal_places = 2
    result = perform_division(dividend_large, divisor_small, decimal_places)
    print(result)