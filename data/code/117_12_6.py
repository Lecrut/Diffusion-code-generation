from decimal import Decimal

class FinancialCalculator:
    def subtract(self, num1, num2):
        return num1 - num2

if __name__ == '__main__':
    calculator = FinancialCalculator()
    result = calculator.subtract(Decimal('10.50'), Decimal('3.25'))
    print(result)