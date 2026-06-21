class MaxFinder:
    def __init__(self, *args):
        self.numbers = args

    def find_max(self):
        return max(self.numbers)

if __name__ == '__main__':
    finder = MaxFinder(10, 5, 20, 8, 15)
    print(finder.find_max())