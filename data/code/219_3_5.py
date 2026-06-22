class MaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        return max(self.numbers)

if __name__ == '__main__':
    finder = MaxFinder((3, 5, 1, 8, 2))
    print(finder.find_max())