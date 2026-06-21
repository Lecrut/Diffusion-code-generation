from decimal import Decimal

def compare_decimals(d1: Decimal, d2: Decimal) -> bool:
    return d1 == d2

if __name__ == '__main__':
    sample_decimal_1 = Decimal('0.1000')
    sample_decimal_2 = Decimal('0.1')
    result = compare_decimals(sample_decimal_1, sample_decimal_2)
    print(f"Comparing {sample_decimal_1} and {sample_decimal_2}: {result}")