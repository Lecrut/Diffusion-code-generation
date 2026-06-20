from decimal import Decimal

def subtract_values(a: float, b: float) -> Decimal:
    return Decimal(str(a)) - Decimal(str(b))

if __name__ == '__main__':
    result = subtract_values(0.1, 0.2)
    print(result)