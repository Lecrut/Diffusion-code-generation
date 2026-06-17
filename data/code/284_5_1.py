def reverse_iterator(iterable):
    for item in reversed(list(iterable)):
        yield item
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_result = list(reverse_iterator(sample_list))
    print(reversed_result)