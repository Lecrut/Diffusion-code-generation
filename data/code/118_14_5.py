from decimal import Decimal
FACTOR_1 = Decimal('10.5')
FACTOR_2 = Decimal('2.3')

def multiply_decimals(a: Decimal, b: Decimal) -> Decimal:
    return a * b
if __name__ == '__main__':
    result = multiply_decimals(FACTOR_1, FACTOR_2)
    print(result)