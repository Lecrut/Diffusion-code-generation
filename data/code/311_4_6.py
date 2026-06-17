def reverse_iterator(iterable):
    for item in reversed(iterable):
        yield item
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(list(reverse_iterator(sample_list)))
    sample_tuple = (6, 7, 8)
    print(list(reverse_iterator(sample_tuple)))
    sample_string = "hello"
    print(list(reverse_iterator(sample_string)))