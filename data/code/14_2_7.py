def get_third_element(data_tuple):
    if not isinstance(data_tuple, tuple):
        raise TypeError("Input must be a tuple")
    if len(data_tuple) < 3:
        raise IndexError("Tuple must contain at least three elements")
    return data_tuple[2]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40)
    print(get_third_element(sample_tuple))