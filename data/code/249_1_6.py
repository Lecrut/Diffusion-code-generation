class LargestFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest(self):
        if not self.numbers:
            raise ValueError("Input list cannot be empty")
        largest = self.numbers[0]
        for number in self.numbers[1:]:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    finder = LargestFinder([15, 8, 22, 4, 30, 11])
    result = finder.find_largest()
    print(result)