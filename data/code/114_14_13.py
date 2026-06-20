class ArithmeticOperations:
    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    calculator = ArithmeticOperations()
    result1 = calculator.multiply(4, 3)
    result2 = calculator.multiply(5, 6)
    print(result1)
    print(result2)