from decimal import Decimal

def validate_input(a: float, b: float) -> None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")

def subtract_values(a: float, b: float) -> Decimal:
    validate_input(a, b)
    return Decimal(str(a)) - Decimal(str(b))

if __name__ == '__main__':
    sample_a = 3.5
    sample_b = 1.25
    result = subtract_values(sample_a, sample_b)
    print(result)