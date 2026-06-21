class NumberComparator:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def calculate_difference(self) -> int:
        return abs(self.num1 - self.num2)

if __name__ == '__main__':
    SAMPLE_NUM1 = 25
    SAMPLE_NUM2 = 9
    comparator = NumberComparator(SAMPLE_NUM1, SAMPLE_NUM2)
    print(comparator.calculate_difference())