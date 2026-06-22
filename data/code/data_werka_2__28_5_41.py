class NumberComparator:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def is_strictly_greater(self) -> bool:
        return self.num1 > self.num2

    def compare_and_report(self) -> bool:
        return self.is_strictly_greater()

if __name__ == '__main__':
    comparator = NumberComparator(6.0, 4.5)
    result1 = comparator.is_strictly_greater()
    result2 = comparator.compare_and_report()
    print("Is num1 strictly greater than num2?", result1)
    print("Compare and report:", result2)