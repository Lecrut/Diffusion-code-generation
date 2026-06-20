from decimal import Decimal

class DecimalOperations:
    def multiply_decimals(self, a: Decimal, b: Decimal) -> Decimal:
        return a * b

if __name__ == '__main__':
    calculator = DecimalOperations()
    result1 = calculator.multiply_decimals(Decimal('10.5'), Decimal('2.3'))
    result2 = calculator.multiply_decimals(Decimal('7.0'), Decimal('3.4'))
    print(result1)
    print(result2)