def reverse_tuple(input_tuple):
    return tuple(reversed(input_tuple))
if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    reversed_sample = reverse_tuple(sample_tuple)
    print(reversed_sample)
    sample_tuple_2 = ('a', 'b', 'c')
    reversed_sample_2 = reverse_tuple(sample_tuple_2)
    print(reversed_sample_2)
    sample_tuple_3 = (10, 20, 30)
    reversed_sample_3 = reverse_tuple(sample_tuple_3)
    print(reversed_sample_3)