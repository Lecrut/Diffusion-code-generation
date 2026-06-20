from decimal import Decimal, getcontext

def precise_division(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be zero')
    getcontext().prec = 28
    dividend_decimal = Decimal(str(dividend))
    divisor_decimal = Decimal(str(divisor))
    result = dividend_decimal / divisor_decimal
    return float(result)
if __name__ == '__main__':
    sample_dividend = 10
    sample_divisor = 3
    print(f'Division of {sample_dividend} by {sample_divisor}: {precise_division(sample_dividend, sample_divisor)}')
    sample_dividend = 15
    sample_divisor = 4
    print(f'Division of {sample_dividend} by {sample_divisor}: {precise_division(sample_dividend, sample_divisor)}')
    sample_dividend = 20
    sample_divisor = 7
    print(f'Division of {sample_dividend} by {sample_divisor}: {precise_division(sample_dividend, sample_divisor)}')