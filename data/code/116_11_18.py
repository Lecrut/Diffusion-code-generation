class SumCalculator:
    A = 10
    B = 25
    C = 40

    @staticmethod
    def calculate_sum():
        return SumCalculator.A + SumCalculator.B + SumCalculator.C

if __name__ == '__main__':
    result = SumCalculator.calculate_sum()
    print(result)