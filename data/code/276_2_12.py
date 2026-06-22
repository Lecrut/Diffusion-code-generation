def repeat_tuple_elements(input_tuple, K):
    if not isinstance(input_tuple, tuple) or not isinstance(K, int):
        raise ValueError('Input must be a tuple and an integer')
    result = input_tuple * K
    return result
if __name__ == '__main__':
    sample_tuple = (1, 2, 3)
    times = 3
    repeated_tuple = repeat_tuple_elements(sample_tuple, times)
    print(repeated_tuple)