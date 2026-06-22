def reverse_tuple(input_tuple):
    return input_tuple[::-1]

if __name__ == '__main__':
    SAMPLE_TUPLE = (3, 2, 1)
    REVERSED_TUPLE = reverse_tuple(SAMPLE_TUPLE)
    print(REVERSED_TUPLE)