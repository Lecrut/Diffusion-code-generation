class SequenceGenerator:
    def generate_sequence(self, n):
        return [i**2 + i for i in range(1, n+1)]

if __name__ == '__main__':
    seq_gen = SequenceGenerator()
    sequence = seq_gen.generate_sequence(10)
    print(sequence)