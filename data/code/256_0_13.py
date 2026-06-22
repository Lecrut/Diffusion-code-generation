class RangeCalculator:
    @staticmethod
    def calculate_range(data):
        if not data:
            return 0.0
        minimum = min(data)
        maximum = max(data)
        return maximum - minimum

if __name__ == '__main__':
    sample_data = [10.5, 3.2, 8.8, 1.1, 5.0]
    range_value = RangeCalculator.calculate_range(sample_data)
    print(range_value)