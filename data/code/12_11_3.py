def get_middle_element_of_tuple(tup):
    if not isinstance(tup, tuple):
        raise TypeError("Input must be a tuple")
    if len(tup) == 0:
        raise ValueError("Tuple must not be empty")
    mid_index = len(tup) // 2
    return tup[mid_index]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = get_middle_element_of_tuple(sample_tuple)
    print(result)