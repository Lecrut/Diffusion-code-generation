import math

class FloatComparator:
    def __init__(self, rel_tol=1e-9, abs_tol=0.0):
        self.rel_tol = rel_tol
        self.abs_tol = abs_tol
    
    def are_close(self, a, b):
        return math.isclose(a, b, rel_tol=self.rel_tol, abs_tol=self.abs_tol)

if __name__ == '__main__':
    comparator = FloatComparator()
    print(comparator.are_close(0.1 + 0.2, 0.3))
    print(comparator.are_close(float('inf'), float('inf')))
    print(comparator.are_close(float('nan'), float('nan')))
    print(comparator.are_close(float('inf'), float('-inf')))