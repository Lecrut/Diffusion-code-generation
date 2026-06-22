class DetermineTheLargestNumberPresentCalculator:
    MAX_NUMBER = 999999

    def find_largest_number(self, numbers):
        if not numbers:
            return None
        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    calculator = DetermineTheLargestNumberPresentCalculator()
    sample_numbers = [123, 456789, 987654, 111111]
    print(f"Largest number: {calculator.find_largest_number(sample_numbers)}")