class NumberComparator:
    DEFAULT_NUM1 = 15
    DEFAULT_NUM2 = 8

    def __init__(self, num1: int = DEFAULT_NUM1, num2: int = DEFAULT_NUM2):
        self.num1 = num1
        self.num2 = num2

    def calculate_difference(self) -> int:
        return abs(self.num1 - self.num2)

if __name__ == '__main__':
    comparator = NumberComparator(20, 10)
    print(comparator.calculate_difference())