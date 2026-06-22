class ArithmeticOperations:
    def add_two_integers(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Both arguments must be integers")
        return a + b

if __name__ == '__main__':
    calculator = ArithmeticOperations()
    result1 = calculator.add_two_integers(15, 27)
    result2 = calculator.add_two_integers(3, 5)
    print(result1)
    print(result2)