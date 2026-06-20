from decimal import Decimal

class PreciseDivision:
    @staticmethod
    def divide(dividend: float, divisor: float) -> Decimal:
        if divisor == 0:
            raise ZeroDivisionError("Divisor cannot be zero")
        return Decimal(dividend) / Decimal(divisor)

if __name__ == '__main__':
    calculator = PreciseDivision()
    result = calculator.divide(10, 3)
    print(result)
    result = calculator.divide(10, 2)
    print(result)
    result = calculator.divide(7, 2)
    print(result)