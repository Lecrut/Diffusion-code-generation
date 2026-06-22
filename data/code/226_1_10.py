import itertools

class SequenceRepeater:
    @staticmethod
    def repeat(sequence, count):
        return list(itertools.chain.from_iterable([sequence] * count))

if __name__ == '__main__':
    repeater = SequenceRepeater()
    sample_sequence = [1, 2, 3]
    n = 3
    result = repeater.repeat(sample_sequence, n)
    print(result)