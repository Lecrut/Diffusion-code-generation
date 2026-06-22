class FloatingPointComparator:
    def __init__(self, tolerance=1e-9):
        self.tolerance = tolerance

    def compare(self, a, b):
        return abs(a - b) <= self.tolerance

if __name__ == '__main__':
    comparator = FloatingPointComparator()
    result = comparator.compare(0.1 + 0.2, 0.3)
    print(result)