class DetermineTheLargestNumberPresentCalculator:
    DEFAULT_MAX = 999999

    @staticmethod
    def find_largest_number(numbers):
        if not numbers:
            return DetermineTheLargestNumberPresentCalculator.DEFAULT_MAX
        return max(numbers)

if __name__ == '__main__':
    calculator = DetermineTheLargestNumberPresentCalculator()
    sample_numbers = [123, 456789, 987654, 111111]
    largest_number = calculator.find_largest_number(sample_numbers)
    print(largest_number)