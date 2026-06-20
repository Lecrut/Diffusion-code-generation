class SumCalculator:
    MAX_NUMBER = 1000

    @staticmethod
    def calculate_total_sum():
        return (SumCalculator.MAX_NUMBER * (SumCalculator.MAX_NUMBER + 1)) // 2

if __name__ == '__main__':
    result = SumCalculator.calculate_total_sum()
    print(result)