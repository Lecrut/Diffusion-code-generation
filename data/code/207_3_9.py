class MaxFinder:
    def __init__(self, data):
        self.data = data

    def find_max(self):
        return max(self.data, default=None)

if __name__ == '__main__':
    finder = MaxFinder([15, 8, 22, 4, 30, 11])
    print(finder.find_max())