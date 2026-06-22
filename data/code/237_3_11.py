class GeometricSequence:
    def __init__(self, start, ratio):
        self.start = float(start)
        self.ratio = float(ratio)

    def generate_sequence(self, terms):
        return [self.start * (self.ratio ** i) for i in range(terms)]

if __name__ == '__main__':
    seq = GeometricSequence(5, 3)
    result = seq.generate_sequence(8)
    print(result)