class ArithmeticOperations:

    def subtract(self, a, b):
        return a - b
if __name__ == '__main__':
    calculator = ArithmeticOperations()
    result1 = calculator.subtract(5, 3)
    result2 = calculator.subtract(10, 7)
    print(result1)
    print(result2)