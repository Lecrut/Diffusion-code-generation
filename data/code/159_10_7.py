class OddNumberFinder:
    def __init__(self):
        self.limit = 50

    def find_odd_numbers(self):
        return [num for num in range(1, self.limit + 1) if num % 2 != 0]

if __name__ == '__main__':
    finder = OddNumberFinder()
    odd_numbers = finder.find_odd_numbers()
    print(odd_numbers)