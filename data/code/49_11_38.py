class LengthComparator:
    DEFAULT_EPSILON = 1e-09

    @staticmethod
    def is_within_tolerance(value1, value2, epsilon):
        return abs(value1 - value2) < epsilon

    def __init__(self, epsilon=None):
        self.epsilon = epsilon if epsilon is not None else LengthComparator.DEFAULT_EPSILON

    def compare(self, length1, length2):
        if not (isinstance(length1, float) and isinstance(length2, float)):
            raise ValueError('Both lengths must be floating-point numbers.')
        if LengthComparator.is_within_tolerance(length1, length2, self.epsilon):
            return None
        elif length1 > length2:
            return length1
        else:
            return length2

if __name__ == '__main__':
    comparator = LengthComparator(epsilon=1e-09)
    length_a = 3.141592653589793
    length_b = 3.141592653589794
    result = comparator.compare(length_a, length_b)
    print(result)