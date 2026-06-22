class SumCalculator:
    CONSTANT_A = 15
    CONSTANT_B = 27

    @staticmethod
    def calculate_sum():
        return SumCalculator.CONSTANT_A + SumCalculator.CONSTANT_B

if __name__ == '__main__':
    result = SumCalculator.calculate_sum()
    print(result)