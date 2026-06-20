import math

class FloatingPointComparator:

    def __init__(self, tolerance=1e-09):
        self.tolerance = tolerance

    def compare_and_return_larger(self, a, b):
        if math.isclose(a, b, rel_tol=self.tolerance):
            return max(a, b)
        else:
            return a if a > b else b
if __name__ == '__main__':
    comparator = FloatingPointComparator()
    result1 = comparator.compare_and_return_larger(0.1 + 0.2, 0.3)
    print(result1)
    result2 = comparator.compare_and_return_larger(1.0, 1.000000001)
    print(result2)