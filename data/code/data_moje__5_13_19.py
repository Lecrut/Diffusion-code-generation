class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = float(length1)
        self.length2 = float(length2)

    def are_equal(self, epsilon=1e-9):
        return abs(self.length1 - self.length2) < epsilon

    def absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator(10.000000001, 10.000000003)
    print(comparator.are_equal())
    print(comparator.absolute_difference())