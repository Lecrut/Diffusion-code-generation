class LucasSequence:
    def __init__(self):
        self.sequence = [2, 1]

    def generate_next(self):
        next_term = self.sequence[-1] + self.sequence[-2]
        self.sequence.append(next_term)

    def get_sequence(self, n):
        while len(self.sequence) < n:
            self.generate_next()
        return self.sequence[:n]

if __name__ == '__main__':
    lucas_seq = LucasSequence()
    sample_terms = 9
    result = lucas_seq.get_sequence(sample_terms)
    print(*result)