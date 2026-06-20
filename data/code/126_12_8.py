import math

class FloatComparator:
    def __init__(self, rel_tol=1e-09, abs_tol=0.0):
        self.rel_tol = rel_tol
        self.abs_tol = abs_tol

    def is_close(self, val1, val2):
        return math.isclose(val1, val2, rel_tol=self.rel_tol, abs_tol=self.abs_tol)

if __name__ == '__main__':
    comparator = FloatComparator()
    print(comparator.is_close(0.1 + 0.2, 0.3))
    print(comparator.is_close(float('inf'), float('inf')))
    print(comparator.is_close(float('nan'), float('nan')))
    print(comparator.is_close(float('inf'), float('-inf')))