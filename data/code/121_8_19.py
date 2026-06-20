from decimal import Decimal
PRECISION = 10

def compare_decimals(value1: Decimal, value2: Decimal) -> bool:
    return abs(value1 - value2) < Decimal('1e-{}'.format(PRECISION))
if __name__ == '__main__':
    sample1 = Decimal('0.123456789')
    sample2 = Decimal('0.123456788')
    result = compare_decimals(sample1, sample2)
    print(result)