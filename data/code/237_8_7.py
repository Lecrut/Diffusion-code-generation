class SequenceGenerator:
    START = 1
    NUM_TERMS = 10

    @staticmethod
    def generate_sequence():
        sequence = [SequenceGenerator.START, SequenceGenerator.START]
        for _ in range(2, SequenceGenerator.NUM_TERMS):
            next_term = sum(sequence[-2:]) + 1
            sequence.append(next_term)
        return sequence

if __name__ == '__main__':
    result = SequenceGenerator.generate_sequence()
    for term in result:
        print(term)