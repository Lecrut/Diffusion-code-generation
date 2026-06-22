class GeometricSequence:
    def __init__(self, start, ratio):
        self.start = start
        self.ratio = ratio

    def generate(self, terms):
        return [self.start * (self.ratio ** i) for i in range(terms)]

if __name__ == '__main__':
    seq = GeometricSequence(5, 3)
    result = seq.generate(8)
    print(result)