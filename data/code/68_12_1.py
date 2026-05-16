class NumberComparator:
    def __init__(self, num1: int, num2: int) -> None:
        self.num1: int = num1
        self.num2: int = num2
    def calculate_difference(self) -> int:
        return self.num1 - self.num2
if __name__ == '__main__':
    comparator = NumberComparator(100, 45)
    difference = comparator.calculate_difference()
    print(difference)