from decimal import Decimal

def precise_division(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    return Decimal(dividend) / Decimal(divisor)

if __name__ == '__main__':
    result = precise_division(10, 3)
    print(result)
    result = precise_division(10, 2)
    print(result)
    result = precise_division(7, 2)
    print(result)