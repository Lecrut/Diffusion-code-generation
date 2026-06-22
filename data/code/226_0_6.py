class NumberRepeater:
    SEQUENCE = list(range(1, 6))
    REPETITIONS = 10

    @staticmethod
    def repeat_sequence(sequence, repetitions):
        result = []
        for element in sequence:
            result.extend([element] * repetitions)
        return result

if __name__ == '__main__':
    repeated_sequence = NumberRepeater.repeat_sequence(NumberRepeater.SEQUENCE, NumberRepeater.REPETITIONS)
    print(repeated_sequence)