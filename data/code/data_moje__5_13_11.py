class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def are_equal(self, epsilon=1e-9):
        return abs(self.length1 - self.length2) < epsilon

    def absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator(1.0000000001, 1.0000000002)
    print(comparator.are_equal())
    print(comparator.absolute_difference())