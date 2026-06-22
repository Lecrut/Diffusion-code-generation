class SequenceGenerator:
    def __init__(self):
        self.sequence = []

    def generate_sequence(self, n):
        for i in range(1, n + 1):
            term = i**2 + i
            self.sequence.append(term)

    def get_sequence(self):
        return self.sequence

if __name__ == '__main__':
    generator = SequenceGenerator()
    generator.generate_sequence(10)
    sequence = generator.get_sequence()
    print(sequence)