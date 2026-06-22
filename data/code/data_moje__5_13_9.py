import math

class LengthComparator:
    def __init__(self):
        self.length1 = 10.0000001
        self.length2 = 10.0000002

    def are_equal_epsilon(self, epsilon=1e-6):
        return abs(self.length1 - self.length2) < epsilon

    def absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.are_equal_epsilon())
    print(comparator.absolute_difference())