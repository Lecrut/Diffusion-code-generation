from decimal import Decimal
DECIMAL_PRECISION = 2

def calculate_monetary_difference(value1: Decimal, value2: Decimal) -> Decimal:
    return (value1 - value2).quantize(Decimal(f'0.{'0' * DECIMAL_PRECISION}'))
if __name__ == '__main__':
    sample_value1 = Decimal('10.50')
    sample_value2 = Decimal('3.25')
    print(calculate_monetary_difference(sample_value1, sample_value2))