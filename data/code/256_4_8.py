class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_range(self):
        return max(self.numbers) - min(self.numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    collection = NumberCollection(sample_numbers)
    print(collection.calculate_range())