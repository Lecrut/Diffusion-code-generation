def repeat_tuple_elements(input_tuple, k):
    if not isinstance(input_tuple, tuple) or not all(isinstance(item, (int, str)) for item in input_tuple):
        raise ValueError("Input must be a tuple of integers and strings")
    if not isinstance(k, int) or k < 1:
        raise ValueError("Repeat count must be a positive integer")

    result = ()
    for element in input_tuple:
        result += (element,) * k
    return result

if __name__ == '__main__':
    sample_tuple = ('a', 'b', 'c')
    repeat_count = 3
    repeated_tuple = repeat_tuple_elements(sample_tuple, repeat_count)
    print(repeated_tuple)