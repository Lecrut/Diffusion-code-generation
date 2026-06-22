import itertools

def validate_input(sequence, count):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a non-negative integer")

def repeat_tuple_elements(tup, n):
    validate_input(tup, n)
    return tuple(itertools.chain.from_iterable(itertools.repeat(x, n) for x in tup))

if __name__ == '__main__':
    sample_tup = (1, 2, 3)
    repetition_count = 4
    result = repeat_tuple_elements(sample_tup, repetition_count)
    print(result)