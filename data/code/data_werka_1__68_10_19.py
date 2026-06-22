class NumberComparator:
    def __init__(self, num1: int, num2: int):
        self.attributes = {'first': num1, 'second': num2}

    def calculate_difference(self) -> int:
        return abs(self.attributes['first'] - self.attributes['second'])

if __name__ == '__main__':
    comparator = NumberComparator(15, 9)
    print(comparator.calculate_difference())