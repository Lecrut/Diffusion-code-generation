class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_range(self):
        if not self.numbers:
            raise ValueError("No numbers provided.")
        minimum = min(self.numbers)
        maximum = max(self.numbers)
        return maximum - minimum

if __name__ == '__main__':
    sample_numbers = [10, 5, 20, 3]
    collection = NumberCollection(sample_numbers)
    range_val = collection.calculate_range()
    print(f"Range: {range_val}")