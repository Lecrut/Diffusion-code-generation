class DetermineTheLargestNumberPresentCalculator:
    MAX_NUMBER = 999999
    @staticmethod
    def find_largest_number(numbers):
        if not numbers:
            return None
        return max(numbers)

if __name__ == '__main__':
    calculator = DetermineTheLargestNumberPresentCalculator()
    sample_numbers = [3, 5, 7, 2, 8, 1]
    largest_number = calculator.find_largest_number(sample_numbers)
    print(largest_number)