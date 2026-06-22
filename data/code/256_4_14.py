class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_range(self):
        if not self.numbers:
            return None
        minimum = min(self.numbers)
        maximum = max(self.numbers)
        range_val = maximum - minimum
        return range_val

if __name__ == '__main__':
    sample_numbers = [10, 5, 20, 3]
    collection = NumberCollection(sample_numbers)
    range_value = collection.calculate_range()
    print(f"Range: {range_value}")