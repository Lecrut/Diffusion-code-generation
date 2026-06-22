class MaxPairFinder:
    def __init__(self, data):
        self.data = data

    def find_max_pairs(self):
        return [max(a, b) for a, b in zip(self.data, self.data[1:])]

if __name__ == '__main__':
    finder = MaxPairFinder([3, 1, 4, 1, 5, 9, 2, 6])
    print(finder.find_max_pairs())