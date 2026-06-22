class SumCalculator:
    NUMBERS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    @staticmethod
    def calculate_sum(numbers):
        return sum(numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    total_sum = calculator.calculate_sum(SumCalculator.NUMBERS)
    print(f"Total Sum: {total_sum}")