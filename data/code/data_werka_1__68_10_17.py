class NumberComparator:
    def __init__(self, number1: int, number2: int):
        self.number1 = number1
        self.number2 = number2

    def calculate_difference(self) -> int:
        return abs(self.number1 - self.number2)

if __name__ == '__main__':
    comparator1 = NumberComparator(15, 8)
    print(comparator1.calculate_difference())

    comparator2 = NumberComparator(20, 10)
    print(comparator2.calculate_difference())