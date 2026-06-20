class MathOperations:
    def multiply(self, a: float, b: float) -> float:
        return a * b

if __name__ == '__main__':
    calculator = MathOperations()
    result1 = calculator.multiply(3.14159, 2.71828)
    result2 = calculator.multiply(4, 3)
    print(result1)
    print(result2)