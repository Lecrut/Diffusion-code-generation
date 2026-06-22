class ComplexNumberFinder:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        if isinstance(number, complex):
            self.numbers.append(number)

    def find_minimum_magnitude(self):
        if not self.numbers:
            return None
        return min(self.numbers, key=abs)

if __name__ == '__main__':
    finder = ComplexNumberFinder()
    finder.add_number(3 + 4j)
    finder.add_number(-1 - 1j)
    finder.add_number(2 + 2j)
    print(finder.find_minimum_magnitude())