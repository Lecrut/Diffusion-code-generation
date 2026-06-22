class NumberFinder:
    def __init__(self):
        self.numbers = []

    def set_numbers(self, numbers):
        self.numbers = numbers

    def find_minimum(self):
        if not self.numbers:
            raise ValueError("The list is empty")
        return min(self.numbers)

if __name__ == '__main__':
    finder = NumberFinder()
    finder.set_numbers([45, 12, 89, 3, 67, 22])
    print(finder.find_minimum())