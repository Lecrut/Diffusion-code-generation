def divide_and_round(dividend, divisor, decimal_places):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = dividend / divisor
    return round(result, decimal_places)

if __name__ == '__main__':
    dividend = 123456789.123456789
    divisor = 12345.6789
    decimal_places = 5
    result = divide_and_round(dividend, divisor, decimal_places)
    print(result)