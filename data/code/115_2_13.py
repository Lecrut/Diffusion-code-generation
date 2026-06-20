from decimal import Decimal

def precise_division(dividend: float, divisor: float) -> Decimal:
    return Decimal(str(dividend)) / Decimal(str(divisor))

if __name__ == '__main__':
    result = precise_division(1.0, 3.0)
    print(result)