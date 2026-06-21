from functools import reduce

class MinFinder:
    def __init__(self, data):
        self.data = data

    def find_min(self):
        if not self.data:
            return None
        return reduce(lambda x, y: x if x < y else y, self.data)

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3, 7]
    finder = MinFinder(sample_list)
    print(finder.find_min())