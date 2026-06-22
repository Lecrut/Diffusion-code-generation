class SumCalculator:
    FIXED_VALUES = (10, 20, 30, 40)

    @staticmethod
    def calculate_sum():
        return sum(SumCalculator.FIXED_VALUES)

if __name__ == '__main__':
    result = SumCalculator.calculate_sum()
    print(result)