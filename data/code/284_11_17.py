def reverse_tuple(input_tuple):
    return input_tuple[::-1]

if __name__ == '__main__':
    SAMPLE_TUPLE = (1, 2, 3, 4, 5)
    reversed_tuple = reverse_tuple(SAMPLE_TUPLE)
    print(reversed_tuple)