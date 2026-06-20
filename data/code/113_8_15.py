class ArithmeticOperations:
    def subtract(self, a, b):
        return a - b

if __name__ == '__main__':
    calculator = ArithmeticOperations()
    print(calculator.subtract(10, 5))
    print(calculator.subtract(5, 10))
    print(calculator.subtract(10, 10))
    print(calculator.subtract(-5, 3))
    print(calculator.subtract(3, -5))
    print(calculator.subtract(-10, -5))
    print(calculator.subtract(-10, -10))