class GeometricSequence:

    def __init__(self, first_term, common_ratio):
        self.first_term = first_term
        self.common_ratio = common_ratio

    def nth_term(self, n):
        return self.first_term * self.common_ratio ** (n - 1)
if __name__ == '__main__':
    seq = GeometricSequence(2, 3)
    print(seq.nth_term(1))
    print(seq.nth_term(2))
    print(seq.nth_term(3))