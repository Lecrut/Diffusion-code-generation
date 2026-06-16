def reverse_iterator(iterable):
    for item in reversed(iterable):
        yield item
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_generator = reverse_iterator(sample_list)
    result_list = list(reversed_generator)
    print(result_list)