class MaxValueFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        return max(self.numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    finder = MaxValueFinder(sample_values)
    print(finder.find_max())