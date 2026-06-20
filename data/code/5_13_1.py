class LengthComparator:
    def __init__(self, length_a, length_b):
        self.length_a = float(length_a)
        self.length_b = float(length_b)

    def is_equal(self, epsilon=1e-9):
        return abs(self.length_a - self.length_b) < epsilon

    def absolute_difference(self):
        return abs(self.length_a - self.length_b)

if __name__ == '__main__':
    comparator = LengthComparator(1.005, 1.0050000001)
    print(comparator.is_equal())
    print(comparator.absolute_difference())