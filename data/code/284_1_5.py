def reverse_tuple(input_tuple):
    return input_tuple[::-1]

if __name__ == '__main__':
    SAMPLE_TUPLE = (10, 20, 30, 40, 50)
    reversed_sample = reverse_tuple(SAMPLE_TUPLE)
    print(reversed_sample)