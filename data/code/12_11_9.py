def get_middle_of_tuple(data):
    if not isinstance(data, tuple):
        raise ValueError("Input must be a tuple")
    if len(data) == 0:
        raise ValueError("Tuple must not be empty")
    mid_index = len(data) // 2
    return data[mid_index]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = get_middle_of_tuple(sample_tuple)
    print(result)