def reverse_iterator(iterable):
    return reversed(iterable)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_iterator_object = reverse_iterator(sample_list)
    result_list = list(reversed_iterator_object)
    print(result_list)