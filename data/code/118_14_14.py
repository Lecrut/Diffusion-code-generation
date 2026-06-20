from decimal import Decimal

def multiply_decimals(a: Decimal, b: Decimal) -> Decimal:
    return a * b

if __name__ == '__main__':
    factor1 = Decimal('3.75')
    factor2 = Decimal('4.80')
    result = multiply_decimals(factor1, factor2)
    print(result)