class SumCalculator:
    NUMBERS_TO_SUM = [5, 7, 9]

    @staticmethod
    def calculate_sum():
        return sum(SumCalculator.NUMBERS_TO_SUM)
if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum()
    print(result)