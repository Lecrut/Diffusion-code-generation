class MinMaxFinder:
    def __init__(self):
        self.minimum = None
        self.maximum = None

    def update(self, number):
        if self.minimum is None or number < self.minimum:
            self.minimum = number
        if self.maximum is None or number > self.maximum:
            self.maximum = number

def find_min_max(numbers):
    finder = MinMaxFinder()
    for number in numbers:
        finder.update(number)
    if finder.minimum is None or finder.maximum is None:
        raise ValueError("Empty list")
    return finder.minimum, finder.maximum

if __name__ == '__main__':
    sample_numbers = [15, 3, 88, 42, 9, 71]
    minimum_val, maximum_val = find_min_max(sample_numbers)
    print(f"Minimum value: {minimum_val}")
    print(f"Maximum value: {maximum_val}")