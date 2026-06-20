from decimal import Decimal
MULTIPLIER = Decimal('2.3')

def multiply_decimals(a: Decimal) -> Decimal:
    return a * MULTIPLIER
if __name__ == '__main__':
    sample_value = Decimal('10.5')
    result = multiply_decimals(sample_value)
    print(result)