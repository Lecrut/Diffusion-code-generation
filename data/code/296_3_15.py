class GeometricSequence:

    def __init__(self, first_term, common_ratio):
        self.first_term = first_term
        self.common_ratio = common_ratio

    @staticmethod
    def nth_term(first_term, common_ratio, n):
        if n <= 0:
            raise ValueError('n must be a positive integer')
        return first_term * common_ratio ** (n - 1)
if __name__ == '__main__':
    seq = GeometricSequence(2, 3)
    print(seq.nth_term(2, 3, 5))