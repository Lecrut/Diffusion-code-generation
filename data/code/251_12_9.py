class DetermineTheLargestNumberPresentCalculator:
    MAX_VALUE = 999999

    @staticmethod
    def find_largest_number(numbers):
        return max(numbers)

if __name__ == '__main__':
    calculator = DetermineTheLargestNumberPresentCalculator()
    sample_numbers = [34, 5678, 123, 90, 8765]
    largest_number = calculator.find_largest_number(sample_numbers)
    print(largest_number)