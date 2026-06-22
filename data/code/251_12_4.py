class DetermineTheLargestNumberPresentCalculator:
    MAX_NUMBER = 999

    @staticmethod
    def find_largest_number(numbers):
        return max(numbers, default=DetermineTheLargestNumberPresentCalculator.MAX_NUMBER)

if __name__ == '__main__':
    calculator = DetermineTheLargestNumberPresentCalculator()
    sample_numbers = [34, 78, 120, 56]
    largest_number = calculator.find_largest_number(sample_numbers)
    print(largest_number)