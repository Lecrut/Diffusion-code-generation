from decimal import Decimal

class FinancialCalculator:
    def subtract(self, value1, value2):
        return value1 - value2

if __name__ == '__main__':
    calculator = FinancialCalculator()
    num_a = Decimal('10.50')
    num_b = Decimal('3.25')
    result = calculator.subtract(num_a, num_b)
    print(result)