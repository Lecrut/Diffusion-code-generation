class NumberSequence:
    MAX_NUMBERS = 10

    @staticmethod
    def generate_sequence(limit):
        return [i**2 for i in range(limit)]

if __name__ == '__main__':
    sequence = NumberSequence.generate_sequence(NumberSequence.MAX_NUMBERS)
    print(sequence)