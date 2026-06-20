class SumDifferenceCalculator:
    @staticmethod
    def calculate(a: int, b: int) -> (int, int):
        return a + b, a - b

if __name__ == '__main__':
    calculator = SumDifferenceCalculator()
    result = calculator.calculate(10, 4)
    print(result)