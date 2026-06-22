class GrowingSequence:
    def __init__(self):
        self.term = 2

    def next_term(self):
        term = round(self.term)
        self.term *= 1.5
        return term

if __name__ == '__main__':
    sequence = GrowingSequence()
    for _ in range(6):
        print(sequence.next_term())