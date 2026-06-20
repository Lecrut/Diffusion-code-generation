class ArithmeticOperations:
    def subtract(self, a: int, b: int) -> int:
        return a - b

if __name__ == '__main__':
    calculator = ArithmeticOperations()
    result1 = calculator.subtract(10, 5)
    result2 = calculator.subtract(7, 3)
    print(result1)
    print(result2)