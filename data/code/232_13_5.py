class GrowingNumberSequence:
    def __init__(self, start=2, multiplier=1.5, terms=6):
        self.start = start
        self.multiplier = multiplier
        self.terms = terms

    def print_sequence(self):
        term = self.start
        for _ in range(self.terms):
            print(round(term))
            term *= self.multiplier

if __name__ == '__main__':
    sequence_instance = GrowingNumberSequence()
    sequence_instance.print_sequence()