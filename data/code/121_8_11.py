from decimal import Decimal

def compare_decimals(a: Decimal, b: Decimal) -> bool:
    return a == b

if __name__ == '__main__':
    sample_a = Decimal('0.12345678901234567890')
    sample_b = Decimal('0.12345678901234567890')
    print(compare_decimals(sample_a, sample_b))