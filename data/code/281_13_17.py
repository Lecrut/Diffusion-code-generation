class SumCalculator:
    NUMBERS = [-10, -5, 0, 5, 10, 15]

    @staticmethod
    def calculate_sum():
        return sum(SumCalculator.NUMBERS)

if __name__ == '__main__':
    result = SumCalculator.calculate_sum()
    print(f"Sum of (-10, -5, 0, 5, 10, 15): {result}")