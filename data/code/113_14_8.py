from decimal import Decimal

def subtract_floats(a: float, b: float) -> Decimal:
    return Decimal(str(a)) - Decimal(str(b))

if __name__ == '__main__':
    result = subtract_floats(1.0, 0.5)
    print(result)