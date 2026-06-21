class NumberFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        return max(self.numbers)

if __name__ == '__main__':
    finder = NumberFinder([10, 5, 22, 8, 30, 15])
    print(finder.find_max())