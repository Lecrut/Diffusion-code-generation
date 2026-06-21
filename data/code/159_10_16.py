class OddNumberFinder:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def find_odd_numbers(self):
        return [num for num in range(self.start, self.end + 1) if num % 2 != 0]

if __name__ == '__main__':
    finder = OddNumberFinder(1, 50)
    odd_numbers = finder.find_odd_numbers()
    print(odd_numbers)