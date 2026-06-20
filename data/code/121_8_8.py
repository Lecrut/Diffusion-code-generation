from decimal import Decimal

def compare_decimals(a: Decimal, b: Decimal) -> str:
    if a == b:
        return "Equal"
    elif a < b:
        return "Less than"
    else:
        return "Greater than"

if __name__ == '__main__':
    sample_a = Decimal('1.2345678901234567890123456789')
    sample_b = Decimal('1.2345678901234567890123456788')
    result = compare_decimals(sample_a, sample_b)
    print(result)