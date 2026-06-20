def precise_division(dividend, divisor, decimal_places):
    if not isinstance(divisor, (int, float)) or divisor == 0:
        raise ValueError("Divisor must be a non-zero number")
    if not isinstance(decimal_places, int) or decimal_places < 0:
        raise ValueError("Decimal places must be a non-negative integer")
    return round(dividend / divisor, decimal_places)

if __name__ == '__main__':
    dividend = 123456789.123456789
    divisor = 7890.123456789
    decimal_places = 5
    result = precise_division(dividend, divisor, decimal_places)
    print(result)