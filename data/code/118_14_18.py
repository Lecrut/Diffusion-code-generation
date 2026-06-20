from decimal import Decimal

def multiply_decimals(a: Decimal, b: Decimal) -> Decimal:
    return a * b

if __name__ == '__main__':
    factor_one = Decimal('15.3')
    factor_two = Decimal('2.7')
    result = multiply_decimals(factor_one, factor_two)
    print(result)