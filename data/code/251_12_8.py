class DetermineTheLargestNumberPresentCalculator:
    MAX_NUMBER = 999999

    @staticmethod
    def find_largest_number(numbers):
        return max(numbers)

if __name__ == '__main__':
    calculator = DetermineTheLargestNumberPresentCalculator()
    sample_numbers = [123, 456789, 987654, 111111]
    print(calculator.find_largest_number(sample_numbers))