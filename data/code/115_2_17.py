from decimal import Decimal
DECIMAL_PRECISION = 28

def precise_division(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be zero')
    return Decimal(dividend).quantize(Decimal('1e-{}').format(DECIMAL_PRECISION)) / Decimal(divisor)
if __name__ == '__main__':
    result = precise_division(10, 3)
    print(result)
    result = precise_division(10, 2)
    print(result)
    result = precise_division(7, 2)
    print(result)