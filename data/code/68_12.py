class NumberComparator:
    def __init__(self, num1: int, num2: int):
        self.num1: int = num1
        self.num2: int = num2
    def calculate_difference(self) -> int:
        return self.num1 - self.num2
if __name__ == '__main__':
    a = 10
    b = 4
    comparator = NumberComparator(a, b)
    difference = comparator.calculate_difference()
    print(difference)