class SumCalculator:
    DEFAULT_X = 15
    DEFAULT_Y = 27

    @staticmethod
    def calculate_sum(x, y):
        return x + y

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum(SumCalculator.DEFAULT_X, SumCalculator.DEFAULT_Y)
    print(result)