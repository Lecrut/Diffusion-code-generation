class MaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        return max(self.numbers)

if __name__ == '__main__':
    sample_values = (3, 5, 1, 8, 2)
    finder = MaxFinder(sample_values)
    max_val = finder.find_max()
    print(max_val)