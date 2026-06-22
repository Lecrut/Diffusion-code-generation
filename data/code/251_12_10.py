class DetermineTheLargestNumberPresentCalculator:
    MAX_NUMBER = 999999

    @staticmethod
    def find_largest_number(numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        return max(numbers)

if __name__ == '__main__':
    calculator = DetermineTheLargestNumberPresentCalculator()
    sample_numbers = [3, 5, 7, 2, 8, 1]
    try:
        largest_number = calculator.find_largest_number(sample_numbers)
        print(largest_number)
    except ValueError as e:
        print(e)