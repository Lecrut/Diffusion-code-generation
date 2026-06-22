class SumCalculator:
    CONSTANT_A = 15
    CONSTANT_B = 27

    @staticmethod
    def sum_constants():
        return SumCalculator.CONSTANT_A + SumCalculator.CONSTANT_B

if __name__ == '__main__':
    print(SumCalculator.sum_constants())