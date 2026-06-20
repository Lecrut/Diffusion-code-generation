from decimal import Decimal

def subtract_values(a: float, b: float) -> Decimal:
    return Decimal(str(a)) - Decimal(str(b))

if __name__ == '__main__':
    result = subtract_values(1.0, 0.9)
    print(result)