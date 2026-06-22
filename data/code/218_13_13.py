class MinFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_min(self):
        return min(self.numbers)

if __name__ == '__main__':
    finder = MinFinder([34, 56, 23, 89, 1])
    print(finder.find_min())