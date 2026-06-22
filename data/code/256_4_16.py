class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers

    def range_of_numbers(self):
        return max(self.numbers) - min(self.numbers)

if __name__ == '__main__':
    sample_numbers = [10, 5, 20, 3]
    collection = NumberCollection(sample_numbers)
    print(f"Range of numbers: {collection.range_of_numbers()}")