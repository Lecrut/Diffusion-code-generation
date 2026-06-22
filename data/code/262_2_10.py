class MinMaxFinder:
    def __init__(self):
        self.numbers = []

    def add_numbers(self, numbers):
        self.numbers.extend(numbers)

    def find_min_max(self):
        if not self.numbers:
            return None, None
        minimum = min(self.numbers)
        maximum = max(self.numbers)
        return minimum, maximum

if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_data1 = [10, 5, 20, 3, 15]
    finder.add_numbers(sample_data1)
    min1, max1 = finder.find_min_max()
    print(f"Data set 1: {sample_data1}")
    print(f"Minimum: {min1}, Maximum: {max1}")