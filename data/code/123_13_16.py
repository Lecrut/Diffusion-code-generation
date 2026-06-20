class SumCalculator:
    START = 1
    END = 100

    @staticmethod
    def calculate_sum():
        return sum(x for x in range(SumCalculator.START, SumCalculator.END + 1))

if __name__ == '__main__':
    result = SumCalculator.calculate_sum()
    print(result)