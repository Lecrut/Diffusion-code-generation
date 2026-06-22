class IntegerSumCalculator:
    def add(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    calculator = IntegerSumCalculator()
    result = calculator.add(5, 3)
    print(result)