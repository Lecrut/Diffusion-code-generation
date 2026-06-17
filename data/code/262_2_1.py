class MinMaxFinder:
    def __init__(self):
        self.numbers = []
    def add_numbers(self, numbers):
        self.numbers.extend(numbers)
    def find_min_max(self):
        if not self.numbers:
            return None, None
        minimum = self.numbers[0]
        maximum = self.numbers[0]
        for number in self.numbers:
            if number < minimum:
                minimum = number
            if number > maximum:
                maximum = number
        return minimum, maximum
if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_data1 = [10, 5, 20, 3, 15]
    finder.add_numbers(sample_data1)
    min1, max1 = finder.find_min_max()
    print(f"Data: {sample_data1}")
    print(f"Minimum: {min1}")
    print(f"Maximum: {max1}")
    finder2 = MinMaxFinder()
    sample_data2 = [-5, 100, 0, -50]
    finder2.add_numbers(sample_data2)
    min2, max2 = finder2.find_min_max()
    print(f"Data: {sample_data2}")
    print(f"Minimum: {min2}")
    print(f"Maximum: {max2}")
    finder3 = MinMaxFinder()
    sample_data3 = []
    finder3.add_numbers(sample_data3)
    min3, max3 = finder3.find_min_max()
    print(f"Data: {sample_data3}")
    print(f"Minimum: {min3}")
    print(f"Maximum: {max3}")