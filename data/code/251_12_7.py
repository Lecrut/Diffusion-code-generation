class DetermineTheLargestNumberPresentCalculator:
    MAX_NUMBER = 999999

    @staticmethod
    def validate_input(numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        for number in numbers:
            if not isinstance(number, (int, float)):
                raise TypeError("All elements must be numbers")

    @staticmethod
    def find_largest_number(numbers):
        DetermineTheLargestNumberPresentCalculator.validate_input(numbers)
        return max(numbers)

if __name__ == '__main__':
    calculator = DetermineTheLargestNumberPresentCalculator()
    sample_numbers = [123, 456789, 987654, 111111]
    largest_number = calculator.find_largest_number(sample_numbers)
    print(largest_number)