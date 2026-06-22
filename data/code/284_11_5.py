def reverse_tuple(input_tuple):
    if not isinstance(input_tuple, tuple):
        raise ValueError("Input must be a tuple")
    return input_tuple[::-1]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    reversed_tuple = reverse_tuple(sample_tuple)
    print(reversed_tuple)