class RangeCalculator:
    @staticmethod
    def calculate_range(numbers):
        if not numbers:
            return None
        minimum = min(numbers)
        maximum = max(numbers)
        return maximum - minimum

if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 8, 15]
    result = RangeCalculator.calculate_range(sample_numbers)
    print(result)