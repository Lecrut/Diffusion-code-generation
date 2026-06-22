class LengthComparator:
    def __init__(self, measurement1, measurement2):
        self.measurement1 = measurement1
        self.measurement2 = measurement2

    def are_equal_within_epsilon(self, epsilon=1e-9):
        difference = abs(self.measurement1 - self.measurement2)
        return difference < epsilon

    def absolute_difference(self):
        return abs(self.measurement1 - self.measurement2)

if __name__ == '__main__':
    comparator = LengthComparator(2.718281828459045, 2.718281828459046)
    print(comparator.are_equal_within_epsilon())
    print(comparator.absolute_difference())