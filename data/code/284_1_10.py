def reverse_tuple(input_tuple):
    return input_tuple[::-1]

if __name__ == '__main__':
    sample_tuple = (6, 5, 4, 3, 2)
    reversed_tuple = reverse_tuple(sample_tuple)
    print(reversed_tuple)