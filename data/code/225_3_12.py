class RangeCalculator:
    @staticmethod
    def calculate_range(numbers):
        if not numbers:
            return None, None
        minimum = min(numbers)
        maximum = max(numbers)
        return minimum, maximum

if __name__ == '__main__':
    sample_data = [10.5, -5.2, 22.3, 0.8, -15.7, 33.4]
    minimum, maximum = RangeCalculator.calculate_range(sample_data)
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")