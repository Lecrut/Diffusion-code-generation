from decimal import Decimal

class PrecisionManager:
    def subtract_values(self, a: float, b: float) -> Decimal:
        return Decimal(str(a)) - Decimal(str(b))

if __name__ == '__main__':
    manager = PrecisionManager()
    result1 = manager.subtract_values(1.0, 0.9)
    print(result1)
    result2 = manager.subtract_values(2.5, 1.25)
    print(result2)