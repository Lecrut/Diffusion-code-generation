from decimal import Decimal

def precise_division(dividend, divisor):
    return Decimal(dividend) / Decimal(divisor)

if __name__ == '__main__':
    result = precise_division(10, 3)
    print(result)