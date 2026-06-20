from decimal import Decimal

def subtract_values(a: float, b: float) -> Decimal:
    return Decimal(str(a)) - Decimal(str(b))

if __name__ == '__main__':
    sample_values = {
        'a': 1.0,
        'b': 0.9
    }
    result = subtract_values(sample_values['a'], sample_values['b'])
    print(result)