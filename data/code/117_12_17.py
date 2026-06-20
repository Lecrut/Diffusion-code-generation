from decimal import Decimal

class FinancialCalculator:
    def subtract(self, num1, num2):
        return num1 - num2

if __name__ == '__main__':
    calculator = FinancialCalculator()
    value1 = Decimal('10.50')
    value2 = Decimal('3.25')
    result = calculator.subtract(value1, value2)
    print(result)