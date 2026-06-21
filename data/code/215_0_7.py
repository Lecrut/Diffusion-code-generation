class NumberFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest(self):
        return max(self.numbers)

if __name__ == '__main__':
    finder = NumberFinder([10, 5, 20, 3, 15])
    largest_number = finder.find_largest()
    print(largest_number)