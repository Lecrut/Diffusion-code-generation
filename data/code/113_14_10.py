from decimal import Decimal

class FloatingPointSubtractor:
    def subtract(self, a: float, b: float) -> Decimal:
        return Decimal(str(a)) - Decimal(str(b))

if __name__ == '__main__':
    subtractor = FloatingPointSubtractor()
    result1 = subtractor.subtract(1.0, 0.9)
    print(result1)
    result2 = subtractor.subtract(2.5, 1.25)
    print(result2)