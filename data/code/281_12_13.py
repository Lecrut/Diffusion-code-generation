class SumCalculator:
    NUMBERS = [1.5, 2.5, 3.5, 4.5, 5.5]

    @staticmethod
    def calculate_sum():
        return sum(SumCalculator.NUMBERS)

if __name__ == '__main__':
    result = SumCalculator.calculate_sum()
    print(result)