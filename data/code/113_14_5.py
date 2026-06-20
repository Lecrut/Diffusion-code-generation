from decimal import Decimal

class PrecisionCalculator:
    @staticmethod
    def subtract_values(a: float, b: float) -> Decimal:
        return Decimal(str(a)) - Decimal(str(b))

if __name__ == '__main__':
    sample_a = 1.0
    sample_b = 0.9
    result = PrecisionCalculator.subtract_values(sample_a, sample_b)
    print(result)