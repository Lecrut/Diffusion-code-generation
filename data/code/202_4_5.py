class MaxFinder:
    def __init__(self, *args):
        self.numbers = list(args)

    def find_max(self):
        return max(self.numbers)

if __name__ == '__main__':
    finder = MaxFinder(3, 5, 1, 2, 4)
    print(finder.find_max())