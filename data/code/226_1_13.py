import itertools

def repeat_sequence(sequence, count):
    return list(itertools.chain.from_iterable([sequence] * count))

if __name__ == '__main__':
    test_seq = [1, 2, 3]
    times = 4
    result = repeat_sequence(test_seq, times)
    print(result)