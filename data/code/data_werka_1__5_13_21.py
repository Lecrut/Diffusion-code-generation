class LengthComparator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def are_equal_within_epsilon(self, epsilon=1e-9):
        return abs(self.value1 - self.value2) < epsilon

    def absolute_difference(self):
        return abs(self.value1 - self.value2)

if __name__ == '__main__':
    comparator = LengthComparator(3.000000001, 3.0)
    print(comparator.are_equal_within_epsilon())
    print(comparator.absolute_difference())