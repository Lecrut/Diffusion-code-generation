import itertools

def repeat_sequence(seq, n):
    return list(itertools.chain.from_iterable([seq] * n))

if __name__ == '__main__':
    sample_seq = [1, 2, 3]
    n = 3
    result = repeat_sequence(sample_seq, n)
    print(result)