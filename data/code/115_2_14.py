from decimal import Decimal

def precise_division(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be zero')
    return Decimal(str(dividend)) / Decimal(str(divisor))
if __name__ == '__main__':
    dividend_val = 15
    divisor_val = 4
    result = precise_division(dividend_val, divisor_val)
    print(result)
    dividend_val = 20
    divisor_val = 7
    result = precise_division(dividend_val, divisor_val)
    print(result)