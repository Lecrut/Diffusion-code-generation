import itertools

class SequenceGenerator:
    REPEAT_CHARS = 'XY'

    @staticmethod
    def generate_sequence(m):
        cycle_iter = itertools.cycle(SequenceGenerator.REPEAT_CHARS)
        return [(i, next(cycle_iter)) for i in range(1, m + 1)]

if __name__ == '__main__':
    sample_output = SequenceGenerator.generate_sequence(5)
    print(sample_output)