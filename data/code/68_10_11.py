class NumberComparator:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def calculate_difference(self) -> float:
        return abs(self.num1 - self.num2)

if __name__ == '__main__':
    comparator = NumberComparator(10.5, 4.2)
    print(comparator.calculate_difference())