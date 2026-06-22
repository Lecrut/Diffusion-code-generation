def reverse_tuple(input_tuple):
    reversed_elements = list(input_tuple)
    reversed_elements.reverse()
    return tuple(reversed_elements)

if __name__ == '__main__':
    sample_tuple = (3, 1, 4, 1, 5, 9)
    reversed_sample_tuple = reverse_tuple(sample_tuple)
    print(reversed_sample_tuple)