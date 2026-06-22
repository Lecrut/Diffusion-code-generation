def reverse_tuple(input_tuple):
    return input_tuple[::-1]

if __name__ == '__main__':
    sample_tuple = (7, 8, 9, 10)
    reversed_tuple = reverse_tuple(sample_tuple)
    print(reversed_tuple)