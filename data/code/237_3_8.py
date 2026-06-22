class GeometricSequenceGenerator:
    def __init__(self, start, ratio):
        self.start = start
        self.ratio = ratio

    def generate_sequence(self, terms):
        return [self.start * (self.ratio ** i) for i in range(terms)]

if __name__ == '__main__':
    generator = GeometricSequenceGenerator(5, 3)
    sequence = generator.generate_sequence(8)
    print(sequence)