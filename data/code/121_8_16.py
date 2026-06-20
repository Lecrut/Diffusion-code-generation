from decimal import Decimal

def compare_decimals(a, b):
    if not isinstance(a, Decimal) or not isinstance(b, Decimal):
        raise ValueError('Both arguments must be instances of Decimal.')
    return a == b
if __name__ == '__main__':
    num1 = Decimal('0.12345678901234567890')
    num2 = Decimal('0.12345678901234567890')
    num3 = Decimal('0.12345678901234567891')
    print(compare_decimals(num1, num2))
    print(compare_decimals(num1, num3))