def get_first_item(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError('The input is not an iterable')
    if isinstance(iterable, (str, bytes)):
        if len(iterable) == 0:
            raise ValueError('The iterable is empty')
    else:
        try:
            iterator = iter(iterable)
            first_item = next(iterator)
            return first_item
        except StopIteration:
            raise ValueError('The iterable is empty')

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4]
    sample_tuple = (5, 6, 7, 8)
    sample_string = 'hello'
    sample_set = {9, 10, 11}
    print(get_first_item(sample_list))
    print(get_first_item(sample_tuple))
    print(get_first_item(sample_string))
    print(get_first_item(sample_set))