class LargestElementFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest(self):
        largest = self.numbers[0]
        for number in self.numbers:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    finder = LargestElementFinder([3.14, 2.718, 1.618, 0.577, 1.414])
    print(finder.find_largest())