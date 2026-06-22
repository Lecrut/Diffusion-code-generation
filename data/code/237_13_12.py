class TriangularNumberSequence:
    MAX_TERMS = 12

    @staticmethod
    def generate_sequence(terms=MAX_TERMS):
        return [n * (n + 1) // 2 for n in range(1, terms + 1)]

if __name__ == '__main__':
    sequence = TriangularNumberSequence.generate_sequence()
    print(sequence)