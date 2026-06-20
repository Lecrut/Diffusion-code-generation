class NumberOperations:
    def subtract(self, a: float, b: float) -> float:
        return a - b

if __name__ == '__main__':
    calculator = NumberOperations()
    result1 = calculator.subtract(25.0, 10.0)
    print(result1)
    result2 = calculator.subtract(7.5, 3.2)
    print(result2)