def reverse_iterator(iterable):
    for item in reversed(iterable):
        yield item
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_generator = reverse_iterator(sample_list)
    result_list = list(reversed_generator)
    print(result_list)
    sample_tuple = (6, 7, 8)
    reversed_generator_tuple = reverse_iterator(sample_tuple)
    result_tuple = list(reversed_generator_tuple)
    print(result_tuple)