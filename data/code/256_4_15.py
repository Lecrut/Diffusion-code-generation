class NumberCollection:
    @staticmethod
    def calculate_range(numbers):
        if not numbers:
            return None
        minimum = min(numbers)
        maximum = max(numbers)
        range_value = maximum - minimum
        return range_value

if __name__ == '__main__':
    sample_numbers = [10, 5, 20, 3]
    range_val = NumberCollection.calculate_range(sample_numbers)
    print(f"Range: {range_val}")