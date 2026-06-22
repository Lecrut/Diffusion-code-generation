import itertools

def repeat_tuple_elements(input_tuple, n):
    return tuple(itertools.chain.from_iterable(itertools.repeat(input_tuple, n)))

if __name__ == '__main__':
    sample_tuple = (1, 2, 3)
    repetition_count = 4
    result = repeat_tuple_elements(sample_tuple, repetition_count)
    print(result)