class LengthComparator:
    DEFAULT_EPSILON = 1e-09

    def __init__(self, epsilon=DEFAULT_EPSILON):
        self.epsilon = epsilon

    def _are_close(self, length1, length2):
        return abs(length1 - length2) < self.epsilon

    def compare(self, length1, length2):
        if not (isinstance(length1, float) and isinstance(length2, float)):
            raise ValueError('Both lengths must be floating-point numbers.')
        if self._are_close(length1, length2):
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

    length_c = 2.718281828459045
    length_d = 2.718281828459046
    result_cd = comparator.compare(length_c, length_d)
    print(result_cd)

    length_e = 1.618033988749895
    length_f = 1.618033988749894
    result_ef = comparator.compare(length_e, length_f)
    print(result_ef)