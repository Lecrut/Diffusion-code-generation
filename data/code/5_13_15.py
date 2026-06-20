class LengthComparator:
    def __init__(self):
        self.length1 = 10.5
        self.length2 = 10.50000001

    def is_equal_within_epsilon(self, epsilon=1e-9):
        return abs(self.length1 - self.length2) < epsilon

    def absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.is_equal_within_epsilon())
    print(comparator.absolute_difference())