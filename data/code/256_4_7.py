class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_range(self):
        return max(self.numbers) - min(self.numbers)

if __name__ == '__main__':
    collection = NumberCollection([10, 20, 30, 40, 50])
    print(collection.calculate_range())