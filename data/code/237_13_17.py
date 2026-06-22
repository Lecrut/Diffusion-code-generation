class TriangularNumberGenerator:
    def generate_sequence(self, n):
        return [(i * (i + 1)) // 2 for i in range(1, n + 1)]

if __name__ == '__main__':
    generator = TriangularNumberGenerator()
    sequence = generator.generate_sequence(12)
    print(sequence)