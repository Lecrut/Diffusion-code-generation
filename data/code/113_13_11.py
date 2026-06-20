class ArithmeticOperations:

    @staticmethod
    def subtract_integers(a: int, b: int) -> int:
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError('Both inputs must be integers')
        return a - b
if __name__ == '__main__':
    calculator = ArithmeticOperations()
    result1 = calculator.subtract_integers(10, 5)
    result2 = calculator.subtract_integers(20, 7)
    print(result1)
    print(result2)