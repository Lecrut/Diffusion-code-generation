import math

class LengthComparator:
    def __init__(self):
        self.length1 = 10.5
        self.length2 = 10.5000000001

    def is_close(self, epsilon=1e-9):
        return math.isclose(self.length1, self.length2, rel_tol=0, abs_tol=epsilon)

    def absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator()
    close_result = comparator.is_close()
    diff_result = comparator.absolute_difference()
    print(close_result)
    print(diff_result)