class FloatComparer:
    def __init__(self, tolerance=1e-9):
        self.tolerance = tolerance

    def are_equal(self, a, b):
        return abs(a - b) <= self.tolerance

if __name__ == '__main__':
    comparer = FloatComparer()
    num1, num2 = 0.1 + 0.2, 0.3
    result = comparer.are_equal(num1, num2)
    print(f"Are {num1} and {num2} equal within tolerance? {result}")