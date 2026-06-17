def reverse_tuple(input_tuple):
    return tuple(reversed(input_tuple))
if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    reversed_sample = reverse_tuple(sample_tuple)
    print(reversed_sample)