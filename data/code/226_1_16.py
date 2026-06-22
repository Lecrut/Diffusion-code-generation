import itertools

def repeat_sequence(sequence, n):
    return list(itertools.chain.from_iterable([sequence] * n))

if __name__ == '__main__':
    sample_sequence = ['x', 'y', 'z']
    repetitions = 4
    result = repeat_sequence(sample_sequence, repetitions)
    print(result)