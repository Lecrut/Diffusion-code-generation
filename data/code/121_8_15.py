from decimal import Decimal

def compare_decimals(a: Decimal, b: Decimal) -> str:
    if a == b:
        return 'Equal'
    else:
        return 'Not Equal'
if __name__ == '__main__':
    sample_a = Decimal('0.12345678901234567890')
    sample_b = Decimal('0.12345678901234567890')
    print(compare_decimals(sample_a, sample_b))
    sample_c = Decimal('0.12345678901234567891')
    sample_d = Decimal('0.12345678901234567890')
    print(compare_decimals(sample_c, sample_d))