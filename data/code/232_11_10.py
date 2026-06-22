class GrowingSequenceGenerator:
    def __init__(self):
        self.sequence = []

    def generate_sequence(self, start, factor, iterations):
        current_term = start
        for _ in range(iterations):
            self.sequence.append(current_term)
            current_term *= factor

    def print_sequence(self):
        for i, term in enumerate(self.sequence, 1):
            print(f"Term {i}: {term}")

if __name__ == '__main__':
    generator = GrowingSequenceGenerator()
    generator.generate_sequence(1, 2, 5)
    generator.print_sequence()