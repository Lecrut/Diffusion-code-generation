from decimal import Decimal

def calculate_monetary_difference(value1: Decimal, value2: Decimal) -> Decimal:
    if not isinstance(value1, Decimal) or not isinstance(value2, Decimal):
        raise ValueError("Both inputs must be instances of Decimal.")
    return value1 - value2

if __name__ == '__main__':
    sample_value1 = Decimal('10.50')
    sample_value2 = Decimal('3.25')
    print(calculate_monetary_difference(sample_value1, sample_value2))