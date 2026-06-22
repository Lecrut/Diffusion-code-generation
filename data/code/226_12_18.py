import itertools

def repeat_tuple_elements(input_tuple, n):
    return tuple(itertools.product(input_tuple, repeat=n))

if __name__ == '__main__':
    sample_tuple = (1, 2)
    repetitions = 3
    result = repeat_tuple_elements(sample_tuple, repetitions)
    print(result)