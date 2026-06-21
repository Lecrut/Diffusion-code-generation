class MaxFinder:
    def __init__(self, data):
        self.data = data

    def find_max(self):
        return max(self.data)

if __name__ == '__main__':
    finder = MaxFinder([3, 1, 4, 1, 5, 9, 2, 6])
    print(finder.find_max())