from decimal import Decimal

def compare_decimals(a: Decimal, b: Decimal) -> str:
    if a == b:
        return "Equal"
    else:
        return "Not Equal"

if __name__ == '__main__':
    sample_a = Decimal('1.0000000000000000000000000001')
    sample_b = Decimal('1.0000000000000000000000000002')
    result = compare_decimals(sample_a, sample_b)
    print(result)