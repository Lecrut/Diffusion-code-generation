from decimal import Decimal

def multiply_decimals(a: Decimal, b: Decimal) -> Decimal:
    return a * b

if __name__ == '__main__':
    factor_a = Decimal('15.2')
    factor_b = Decimal('3.7')
    result = multiply_decimals(factor_a, factor_b)
    print(result)