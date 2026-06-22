def reverse_tuple(input_tuple):
    if not isinstance(input_tuple, tuple):
        raise ValueError("Input must be a tuple")
    return input_tuple[::-1]

if __name__ == '__main__':
    sample_tuple = (5, 4, 3, 2, 1)
    reversed_tuple = reverse_tuple(sample_tuple)
    print(reversed_tuple)