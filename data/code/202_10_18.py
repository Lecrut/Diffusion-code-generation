class NumberFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_largest_number(self):
        if not self.numbers:
            return None
        return max(self.numbers)

if __name__ == '__main__':
    finder1 = NumberFinder([10, 5, 22, 8, 3])
    print(finder1.get_largest_number())

    finder2 = NumberFinder([-1, -5, -22, -8, -3])
    print(finder2.get_largest_number())

    finder3 = NumberFinder([1.5, 2.5, 0.5, -1.5])
    print(finder3.get_largest_number())