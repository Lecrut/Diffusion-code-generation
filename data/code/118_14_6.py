from decimal import Decimal

def multiply_decimals(a: Decimal, b: Decimal) -> Decimal:
    return a * b

if __name__ == '__main__':
    value1 = Decimal('25.0')
    value2 = Decimal('3.4')
    result = multiply_decimals(value1, value2)
    print(result)