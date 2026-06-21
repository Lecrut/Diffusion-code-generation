from functools import reduce

class MinFinder:
    def find_min(self, numbers):
        return reduce(lambda x, y: x if x < y else y, numbers)

if __name__ == '__main__':
    sample_values = [4, 7, 1, 3, 9]
    min_finder = MinFinder()
    print(min_finder.find_min(sample_values))