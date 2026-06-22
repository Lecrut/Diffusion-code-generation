class NumberSequence:
    LIMIT = 10

    @staticmethod
    def generate_sequence(limit):
        sequence = []
        for i in range(limit):
            sequence.append(i**2)
        return sequence

if __name__ == '__main__':
    sequence = NumberSequence.generate_sequence(NumberSequence.LIMIT)
    print(sequence)