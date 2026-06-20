class LengthComparator:
    def __init__(self, length_a, length_b):
        self.length_a = length_a
        self.length_b = length_b
        self.epsilon = 1e-9

    def is_equal_within_epsilon(self):
        return abs(self.length_a - self.length_b) < self.epsilon

    def get_absolute_difference(self):
        return abs(self.length_a - self.length_b)

if __name__ == '__main__':
    comparator = LengthComparator(10.000000001, 10.0)
    print(comparator.is_equal_within_epsilon())
    print(comparator.get_absolute_difference())