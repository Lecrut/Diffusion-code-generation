class NumberRangeCalculator:
    def calculate_range(self, numbers):
        if not numbers:
            return 0.0
        minimum = min(numbers)
        maximum = max(numbers)
        return maximum - minimum

if __name__ == '__main__':
    calculator = NumberRangeCalculator()
    sample_data = [10.5, 2.1, 8.0, 4.9, 15.7]
    range_value = calculator.calculate_range(sample_data)
    print(range_value)