from decimal import Decimal

def validate_inputs(a: Decimal, b: Decimal) -> None:
    if not isinstance(a, Decimal) or not isinstance(b, Decimal):
        raise TypeError("Both arguments must be instances of Decimal")

def multiply_decimals(a: Decimal, b: Decimal) -> Decimal:
    validate_inputs(a, b)
    return a * b

if __name__ == '__main__':
    sample_a = Decimal('10.5')
    sample_b = Decimal('2.3')
    result = multiply_decimals(sample_a, sample_b)
    print(result)