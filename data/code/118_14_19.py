from decimal import Decimal

class DecimalCalculator:
    def multiply_decimals(self, a: Decimal, b: Decimal) -> Decimal:
        return a * b

if __name__ == '__main__':
    calculator = DecimalCalculator()
    result1 = calculator.multiply_decimals(Decimal('10.5'), Decimal('2.3'))
    result2 = calculator.multiply_decimals(Decimal('5.0'), Decimal('4.2'))
    print(result1)
    print(result2)