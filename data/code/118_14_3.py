from decimal import Decimal

def multiply_decimals(a: Decimal, b: Decimal) -> Decimal:
    if not isinstance(a, Decimal) or not isinstance(b, Decimal):
        raise TypeError("Both arguments must be instances of Decimal")
    return a * b

if __name__ == '__main__':
    try:
        result = multiply_decimals(Decimal('10.5'), Decimal('2.3'))
        print(result)
    except Exception as e:
        print(e)