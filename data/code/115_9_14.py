def divide_and_round(dividend, divisor, decimal_places):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = dividend / divisor
    return round(result, decimal_places)

if __name__ == '__main__':
    sample_dividend = 123456789.123456789
    sample_divisor = 12345.6789
    sample_decimal_places = 4
    result = divide_and_round(sample_dividend, sample_divisor, sample_decimal_places)
    print(result)