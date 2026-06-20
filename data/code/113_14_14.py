from decimal import Decimal

class PrecisionSubtractor:
    def subtract(self, a: float, b: float) -> Decimal:
        return Decimal(str(a)) - Decimal(str(b))

if __name__ == '__main__':
    subtractor = PrecisionSubtractor()
    result1 = subtractor.subtract(1.0, 0.9)
    print(result1)
    result2 = subtractor.subtract(1.0, 0.1)
    print(result2)
    result3 = subtractor.subtract(2.0, 1.75)
    print(result3)
    result4 = subtractor.subtract(1.0, 0.5)
    print(result4)