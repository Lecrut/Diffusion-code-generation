import itertools
REPEAT_FACTOR = 3

def repeat_tuple_elements(tup):
    return tuple(itertools.chain.from_iterable((itertools.repeat(x, REPEAT_FACTOR) for x in tup)))
if __name__ == '__main__':
    sample_tup = (1, 2)
    result = repeat_tuple_elements(sample_tup)
    print(result)