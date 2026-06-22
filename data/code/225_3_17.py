class RangeCalculator:
    @staticmethod
    def calculate_range(numbers):
        if not numbers:
            return None, None
        minimum = min(numbers)
        maximum = max(numbers)
        return minimum, maximum

if __name__ == '__main__':
    sample_values = [10.5, -3.2, 7.8, 0.0, -6.4, 23.1]
    minimum, maximum = RangeCalculator.calculate_range(sample_values)
    print(f"Range: {maximum - minimum}")