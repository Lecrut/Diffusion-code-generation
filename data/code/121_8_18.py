from decimal import Decimal

def compare_decimals(a: Decimal, b: Decimal) -> str:
    if a == b:
        return "Equal"
    elif a < b:
        return "Less than"
    else:
        return "Greater than"

if __name__ == '__main__':
    sample_a = Decimal('1234567890.12345678901234567890')
    sample_b = Decimal('1234567890.12345678901234567891')
    result = compare_decimals(sample_a, sample_b)
    print(result)