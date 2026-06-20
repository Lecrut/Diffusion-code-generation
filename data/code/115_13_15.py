from decimal import Decimal, getcontext

def divide_decimals(a: Decimal, b: Decimal) -> Decimal:
    if b == Decimal('0'):
        raise ValueError("Cannot divide by zero")
    getcontext().prec = 50
    result = a / b
    return result

if __name__ == '__main__':
    try:
        result = divide_decimals(Decimal('1.234567890123456789012345678901234567890123456789'), Decimal('2.345678901234567890123456789012345678901234567890'))
        print(result)
    except ValueError as e:
        print(e)