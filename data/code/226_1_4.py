import itertools

def repeat_sequence(sequence, n):
    return list(itertools.chain.from_iterable([sequence] * n))

if __name__ == '__main__':
    start_seq = ['x', 'y', 'z']
    rep_count = 4
    output = repeat_sequence(start_seq, rep_count)
    print(output)