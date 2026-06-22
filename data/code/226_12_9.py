import itertools

def repeat_tuple_elements(tup, n):
    return tuple(itertools.chain.from_iterable(itertools.repeat(x, n) for x in tup))

if __name__ == '__main__':
    sample_tup = (4, 5)
    repetition_count = 2
    result = repeat_tuple_elements(sample_tup, repetition_count)
    print(result)