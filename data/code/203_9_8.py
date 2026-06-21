class NumberComparer:

    def __init__(self, tolerance=1e-09):
        self.tolerance = tolerance

    def are_close(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance
if __name__ == '__main__':
    comparer = NumberComparer(tolerance=1e-07)
    result1 = comparer.are_close(0.1 + 0.2, 0.3)
    result2 = comparer.are_close(1.0, 1.00000001)
    print(result1)
    print(result2)