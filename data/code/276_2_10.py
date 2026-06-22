def repeat_tuple_elements(tup, k):
    if not isinstance(tup, tuple) or not all(isinstance(x, (int, str)) for x in tup):
        raise ValueError("Input must be a tuple of integers and/or strings")
    if not isinstance(k, int) or k < 0:
        raise ValueError("K must be a non-negative integer")

    result = ()
    for element in tup:
        repeated_element = (element,) * k
        result += repeated_element

    return result

if __name__ == '__main__':
    sample_tuple = ('a', 'b', 'c')
    repeat_count = 3
    repeated_tuple = repeat_tuple_elements(sample_tuple, repeat_count)
    print(repeated_tuple)