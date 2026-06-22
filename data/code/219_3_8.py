class MaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        return max(self.numbers)

if __name__ == '__main__':
    sample_numbers = (3, 5, 1, 8, 2)
    finder = MaxFinder(sample_numbers)
    max_val = finder.find_max()
    print(max_val)