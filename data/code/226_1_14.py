import itertools

def repeat_sequence(sequence, n):
    return list(itertools.chain.from_iterable([sequence] * n))

if __name__ == '__main__':
    sample_sequence = [1, 2, 3]
    n = 3
    print(repeat_sequence(sample_sequence, n))