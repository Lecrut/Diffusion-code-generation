class GeometricSequence:
    def __init__(self):
        self.sequence = [1]

    def generate(self, iterations):
        for _ in range(iterations - 1):
            self.sequence.append(self.sequence[-1] * 3)

if __name__ == '__main__':
    generator = GeometricSequence()
    generator.generate(8)
    print(generator.sequence)