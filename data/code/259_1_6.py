class MinMaxFinder:
    def __init__(self, data):
        self.data = data

    def find_min_max(self):
        return min(self.data), max(self.data)

if __name__ == '__main__':
    finder = MinMaxFinder([3, 1, 4, 1, 5, 9, 2, 6])
    minimum, maximum = finder.find_min_max()
    print((minimum, maximum))