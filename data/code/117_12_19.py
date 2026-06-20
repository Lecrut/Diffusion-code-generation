from decimal import Decimal

class ValueSubtractor:
    def subtract(self, value1: Decimal, value2: Decimal) -> Decimal:
        return value1 - value2

if __name__ == '__main__':
    subtrator = ValueSubtractor()
    sample_value1 = Decimal('10.5')
    sample_value2 = Decimal('3.25')
    result = subtrator.subtract(sample_value1, sample_value2)
    print(result)