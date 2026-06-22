import itertools

def repeat_tuple_elements(tup, n):
    if not isinstance(tup, tuple) or not all(isinstance(x, (int, float)) for x in tup):
        raise ValueError("First argument must be a tuple of numbers")
    if not isinstance(n, int) or n < 0:
        raise ValueError("Second argument must be a non-negative integer")
    
    return tuple(itertools.chain.from_iterable(itertools.repeat(x, n) for x in tup))

if __name__ == '__main__':
    sample_tup = (1.5, 2.5, 3)
    repetition_count = 3
    result = repeat_tuple_elements(sample_tup, repetition_count)
    print(result)