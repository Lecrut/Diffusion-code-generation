class NumberComparator:
    def __init__(self, num1: int, num2: int):
        self.numbers = {'first': num1, 'second': num2}

    def calculate_difference(self) -> int:
        return abs(self.numbers['first'] - self.numbers['second'])

if __name__ == '__main__':
    comparator = NumberComparator(7, 3)
    print(comparator.calculate_difference())