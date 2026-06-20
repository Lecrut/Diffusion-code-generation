import math

def divide_and_round(dividend, divisor, decimal_places):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = dividend / divisor
    return round(result, decimal_places)

if __name__ == '__main__':
    numerator = 123456789.123456789
    denominator = 12345
    decimals = 5
    output = divide_and_round(numerator, denominator, decimals)
    print(output)