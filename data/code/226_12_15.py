import itertools

def repeat_tuple_elements(tup, n):
    return tuple(itertools.chain.from_iterable(itertools.repeat(x, n) for x in tup))

if __name__ == '__main__':
    SAMPLE_TUP = (1, 2)
    REPETITION_COUNT = 3
    result = repeat_tuple_elements(SAMPLE_TUP, REPETITION_COUNT)
    print(result)