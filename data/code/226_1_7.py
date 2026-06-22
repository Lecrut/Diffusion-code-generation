import itertools

def validate_sequence(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Input must be a list or tuple")

def validate_count(count):
    if not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a non-negative integer")

def repeat_sequence(sequence, n):
    validate_sequence(sequence)
    validate_count(n)
    return list(itertools.chain.from_iterable([sequence] * n))

if __name__ == '__main__':
    sample_sequence = [1, 2, 3]
    count = 3
    result = repeat_sequence(sample_sequence, count)
    print(result)