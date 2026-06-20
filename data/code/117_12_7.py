from decimal import Decimal

class FinancialCalculator:
    def subtract(self, num1, num2):
        return num1 - num2

if __name__ == '__main__':
    calculator = FinancialCalculator()
    value_a = Decimal('10.50')
    value_b = Decimal('3.25')
    result = calculator.subtract(value_a, value_b)
    print(result)