class NumberComparer:
    def __init__(self, tolerance=1e-9):
        self.tolerance = tolerance

    def are_close(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance

if __name__ == '__main__':
    comparer = NumberComparer(1e-7)
    result1 = comparer.are_close(0.1 + 0.2, 0.3)
    print(result1)
    result2 = comparer.are_close(0.5, 0.500000001)
    print(result2)