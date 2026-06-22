def reverse_tuple(input_tuple):
    return input_tuple[::-1]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    reversed_tuple = reverse_tuple(sample_tuple)
    print(reversed_tuple)