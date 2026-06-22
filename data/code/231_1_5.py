import itertools

class SequenceGenerator:
    REPEAT_PATTERN = [1, 2, 3]

    @staticmethod
    def generate_sequence(length):
        return list(itertools.islice(itertools.cycle(SequenceGenerator.REPEAT_PATTERN), length))

if __name__ == '__main__':
    sample_length = 15
    result = SequenceGenerator.generate_sequence(sample_length)
    print(result)