from itertools import product

def repeat_tuple_elements(input_tuple, n):
    return tuple(product(input_tuple, repeat=n))

if __name__ == '__main__':
    sample_tuple = (1, 2)
    repetition_count = 3
    result = repeat_tuple_elements(sample_tuple, repetition_count)
    print(result)