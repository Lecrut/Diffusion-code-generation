from decimal import Decimal

class ValueCalculator:
    def subtract(self, num1: Decimal, num2: Decimal) -> Decimal:
        return num1 - num2

if __name__ == '__main__':
    calculator = ValueCalculator()
    value_a = Decimal('10.5')
    value_b = Decimal('3.2')
    result = calculator.subtract(value_a, value_b)
    print(result)