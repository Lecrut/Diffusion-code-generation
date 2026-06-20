from decimal import Decimal

class FinancialCalculator:
    def subtract_values(self, value1, value2):
        return value1 - value2

if __name__ == '__main__':
    calculator = FinancialCalculator()
    result = calculator.subtract_values(Decimal('10.5'), Decimal('3.2'))
    print(result)