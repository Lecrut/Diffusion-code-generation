from decimal import Decimal

class DecimalOperations:
    @staticmethod
    def multiply_decimals(a: Decimal, b: Decimal) -> Decimal:
        return a * b

if __name__ == '__main__':
    result = DecimalOperations.multiply_decimals(Decimal('10.5'), Decimal('2.3'))
    print(result)