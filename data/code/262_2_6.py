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
    sample_data1 = [10, 5, 20, 15, 3]
    finder.add_numbers(sample_data1)
    min_val1, max_val1 = finder.find_min_max()
    print(f"Data: {sample_data1}")
    print(f"Minimum: {min_val1}")
    print(f"Maximum: {max_val1}")
    finder2 = MinMaxFinder()
    sample_data2 = [100, -50, 75, 0, 120]
    finder2.add_numbers(sample_data2)
    min_val2, max_val2 = finder2.find_min_max()
    print(f"\nData: {sample_data2}")
    print(f"Minimum: {min_val2}")
    print(f"Maximum: {max_val2}")
    finder3 = MinMaxFinder()
    sample_data3 = []
    finder3.add_numbers(sample_data3)
    min_val3, max_val3 = finder3.find_min_max()
    print(f"\nData: {sample_data3}")
    print(f"Minimum: {min_val3}")
    print(f"Maximum: {max_val3}")