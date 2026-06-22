class TriangularNumberGenerator:
    def __init__(self):
        self.sequence = []

    def generate_next(self):
        if not self.sequence:
            self.sequence.append(1)
        else:
            next_value = sum(range(1, len(self.sequence) + 2))
            self.sequence.append(next_value)

    def get_sequence(self):
        return self.sequence

if __name__ == '__main__':
    generator = TriangularNumberGenerator()
    for _ in range(12):
        generator.generate_next()

    print(generator.get_sequence())