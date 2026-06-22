class GrowingSequence:
    def __init__(self, start=1, factor=2):
        self.start = start
        self.factor = factor

    def generate_sequence(self, iterations):
        sequence = []
        current_term = self.start
        for _ in range(iterations):
            sequence.append(current_term)
            current_term *= self.factor
        return sequence

if __name__ == '__main__':
    seq_gen = GrowingSequence(start=1, factor=2)
    sequence = seq_gen.generate_sequence(5)
    for term in sequence:
        print(term)