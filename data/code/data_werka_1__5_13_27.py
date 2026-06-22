class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def are_equal_within_epsilon(self, epsilon=1e-9):
        return abs(self.length1 - self.length2) < epsilon

    def absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator(3.141592653589793, 3.14159265358979)
    print(comparator.are_equal_within_epsilon())
    print(comparator.absolute_difference())