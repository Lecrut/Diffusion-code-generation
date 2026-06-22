from functools import reduce

class MaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        return reduce(lambda x, y: x if x > y else y, self.numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    finder = MaxFinder(sample_numbers)
    print(finder.find_max())