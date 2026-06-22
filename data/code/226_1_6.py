import itertools

def repeat_sequence(sequence, count):
    return list(itertools.chain.from_iterable([sequence] * count))

if __name__ == '__main__':
    sample_sequence = [1, 2, 3]
    n = 3
    result = repeat_sequence(sample_sequence, n)
    print(result)