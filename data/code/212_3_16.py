class MinMaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_min_max(self):
        return min(self.numbers), max(self.numbers)

if __name__ == '__main__':
    finder = MinMaxFinder([15, 3, 88, 42, 9, 71])
    minimum_val, maximum_val = finder.find_min_max()
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")