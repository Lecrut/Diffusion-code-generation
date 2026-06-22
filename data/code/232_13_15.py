class GrowingSequence:
    def __init__(self):
        self.term = 2

    def next_term(self):
        result = round(self.term)
        self.term *= 1.5
        return result

if __name__ == '__main__':
    seq = GrowingSequence()
    for _ in range(6):
        print(seq.next_term())