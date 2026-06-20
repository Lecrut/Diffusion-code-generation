class ArithmeticOperations:
    def subtract(self, a, b):
        return a - b

if __name__ == '__main__':
    calc = ArithmeticOperations()
    print(calc.subtract(10, 5))
    print(calc.subtract(5, 10))
    print(calc.subtract(10, 10))
    print(calc.subtract(-10, 5))
    print(calc.subtract(5, -10))
    print(calc.subtract(-10, -5))
    print(calc.subtract(-10, -10))