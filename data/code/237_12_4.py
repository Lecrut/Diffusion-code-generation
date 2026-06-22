class GeometricSequenceGenerator:
    def __init__(self):
        self.sequence = [1]

    def generate_sequence(self, iterations):
        for _ in range(iterations):
            self.sequence.append(self.sequence[-1] * 3)

    def get_sequence(self):
        return self.sequence

if __name__ == '__main__':
    generator = GeometricSequenceGenerator()
    generator.generate_sequence(8)
    print(generator.get_sequence())