class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_range(self):
        return max(self.numbers) - min(self.numbers)

if __name__ == '__main__':
    sample_numbers = [12, 34, 56, 78, 90, 1]
    collection = NumberCollection(sample_numbers)
    range_val = collection.calculate_range()
    print(f"Range of numbers: {range_val}")