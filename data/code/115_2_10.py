import decimal

def precise_division(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    return float(decimal.Decimal(dividend) / decimal.Decimal(divisor))

if __name__ == '__main__':
    result = precise_division(10, 3)
    print(result)