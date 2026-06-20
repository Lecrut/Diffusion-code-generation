from decimal import Decimal

def calculate_difference(value1: Decimal, value2: Decimal) -> Decimal:
    return value1 - value2

if __name__ == '__main__':
    sample_value1 = Decimal('10.50')
    sample_value2 = Decimal('5.25')
    result = calculate_difference(sample_value1, sample_value2)
    print(result)