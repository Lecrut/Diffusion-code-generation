class LengthComparator:
    DEFAULT_EPSILON = 1e-09

    @staticmethod
    def are_close(a, b, tol):
        return abs(a - b) < tol

    def __init__(self, epsilon=DEFAULT_EPSILON):
        self.epsilon = epsilon

    def compare(self, length1, length2):
        if not (isinstance(length1, float) and isinstance(length2, float)):
            raise ValueError('Both lengths must be floating-point numbers.')
        if LengthComparator.are_close(length1, length2, self.epsilon):
            return None
        elif length1 > length2:
            return length1
        else:
            return length2

if __name__ == '__main__':
    comparator = LengthComparator(epsilon=1e-09)
    length_a = 2.718281828459045
    length_b = 2.718281828459046
    result = comparator.compare(length_a, length_b)
    print(result)