class GrowingSequence:
    def __init__(self, start=2):
        self.current_term = start

    def next_term(self):
        result = round(self.current_term)
        self.current_term *= 1.5
        return result

if __name__ == '__main__':
    seq = GrowingSequence()
    for _ in range(6):
        print(seq.next_term())