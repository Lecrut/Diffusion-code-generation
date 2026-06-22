class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers

    @staticmethod
    def from_string(input_line):
        return NumberCollection([float(x) for x in input_line.split()])

    def calculate_range(self):
        if not self.numbers:
            raise ValueError("No numbers provided.")
        minimum = min(self.numbers)
        maximum = max(self.numbers)
        return maximum - minimum

if __name__ == '__main__':
    collection = NumberCollection.from_string("10 5 20 3")
    range_val = collection.calculate_range()
    print(f"Range: {range_val}")