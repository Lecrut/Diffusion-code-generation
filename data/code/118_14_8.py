from decimal import Decimal

class DecimalProductCalculator:
    def calculate_product(self, a: Decimal, b: Decimal) -> Decimal:
        return a * b

if __name__ == '__main__':
    calculator = DecimalProductCalculator()
    result1 = calculator.calculate_product(Decimal('10.5'), Decimal('2.3'))
    result2 = calculator.calculate_product(Decimal('5.0'), Decimal('4.2'))
    print(result1)
    print(result2)