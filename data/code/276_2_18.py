def repeat_tuple_elements(input_tuple, k):
    if not isinstance(input_tuple, tuple) or not all((isinstance(item, (int, float, str)) for item in input_tuple)):
        raise ValueError('Input must be a tuple of integers, floats, or strings')
    if not isinstance(k, int) or k < 0:
        raise ValueError('K must be a non-negative integer')
    result = ()
    for element in input_tuple:
        repeated_elements = (element,) * k
        result += repeated_elements
    return result
if __name__ == '__main__':
    sample_tuple = ('a', 'b', 'c')
    times = 3
    repeated_result = repeat_tuple_elements(sample_tuple, times)
    print(repeated_result)