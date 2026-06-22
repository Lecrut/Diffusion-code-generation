def repeat_tuple_elements(input_tuple, k):
    if not isinstance(input_tuple, tuple) or not all(isinstance(item, (int, float, str)) for item in input_tuple):
        raise ValueError("Input must be a tuple of integers, floats, or strings")
    if not isinstance(k, int) or k < 0:
        raise ValueError("K must be a non-negative integer")
    
    return input_tuple * k

if __name__ == '__main__':
    sample_tuple = (1, 2, "a", "b")
    repeat_count = 3
    result = repeat_tuple_elements(sample_tuple, repeat_count)
    print(result)