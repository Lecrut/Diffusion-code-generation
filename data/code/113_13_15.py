class IntegerCalculator:
    MIN_INT = -2147483648
    MAX_INT = 2147483647

    @staticmethod
    def subtract_integers(a: int, b: int) -> int:
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Both inputs must be integers")
        if a < IntegerCalculator.MIN_INT or a > IntegerCalculator.MAX_INT or b < IntegerCalculator.MIN_INT or b > IntegerCalculator.MAX_INT:
            raise OverflowError("Inputs are out of integer range")
        return a - b

if __name__ == '__main__':
    calculator = IntegerCalculator()
    result = calculator.subtract_integers(10, 5)
    print(result)