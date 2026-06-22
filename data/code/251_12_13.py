class DetermineTheLargestNumberPresentCalculator:
    MAX_VALUE = float('inf')

    @staticmethod
    def find_largest_number(numbers):
        return max(numbers, default=DetermineTheLargestNumberPresentCalculator.MAX_VALUE)

if __name__ == '__main__':
    calculator = DetermineTheLargestNumberPresentCalculator()
    sample_numbers = [3, 5, 1, 2, 4]
    print(calculator.find_largest_number(sample_numbers))