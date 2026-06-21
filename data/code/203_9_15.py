class NumberComparator:
    def __init__(self, tolerance=1e-9):
        self.tolerance = tolerance

    def are_close(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance

if __name__ == '__main__':
    comparator = NumberComparator(1e-7)
    result1 = comparator.are_close(0.1 + 0.2, 0.3)
    result2 = comparator.are_close(1.0000001, 1.0)
    print(result1, result2)