class NumberSequence:
    def __init__(self):
        self.sequence = []

    def generate_sequence(self, limit):
        for i in range(limit):
            self.sequence.append(i**2)

    def get_sequence(self):
        return self.sequence

if __name__ == '__main__':
    seq_gen = NumberSequence()
    seq_gen.generate_sequence(10)
    print(seq_gen.get_sequence())