class LengthComparator:
    DEFAULT_EPSILON = 1e-9

    def __init__(self, length1=3.141592653589793, length2=3.1415926535897932):
        self.length1 = length1
        self.length2 = length2

    def are_equal_within_epsilon(self, epsilon=DEFAULT_EPSILON):
        return abs(self.length1 - self.length2) < epsilon

    def absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator(3.0000000005, 3.000000001)
    print(comparator.are_equal_within_epsilon())
    print(comparator.absolute_difference())