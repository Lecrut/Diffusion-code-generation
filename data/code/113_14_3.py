from decimal import Decimal

def subtract_values(a: float, b: float) -> Decimal:
    return Decimal(str(a)) - Decimal(str(b))

if __name__ == '__main__':
    sample_a = 2.0
    sample_b = 1.75
    result = subtract_values(sample_a, sample_b)
    print(result)