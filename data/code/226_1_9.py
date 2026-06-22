import itertools

def repeat_sequence(sequence, count):
    if not isinstance(sequence, (list, tuple, str)):
        raise ValueError('sequence must be a list, tuple, or string')
    if not isinstance(count, int) or count < 0:
        raise ValueError('count must be a non-negative integer')
    return list(itertools.chain.from_iterable([sequence] * count))
if __name__ == '__main__':
    sample_sequence = [1, 2, 3]
    n = 3
    result = repeat_sequence(sample_sequence, n)
    print(result)