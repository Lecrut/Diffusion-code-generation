import itertools

def validate_sequence(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Input must be a list or tuple")

def repeat_sequence(sequence, count):
    validate_sequence(sequence)
    return list(itertools.chain.from_iterable([sequence] * count))

if __name__ == '__main__':
    sample_sequence = [1, 2, 3]
    n = 3
    result = repeat_sequence(sample_sequence, n)
    print(result)