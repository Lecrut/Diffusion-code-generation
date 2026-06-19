def get_first_item(iterable):
    iterator = iter(iterable)
    first_value = next(iterator, None)
    return first_value
if __name__ == '__main__':
    sample_tuple = (7, 8, 9)
    sample_string = 'world'
    empty_set = set()
    print(get_first_item(sample_tuple))
    print(get_first_item(sample_string))
    print(get_first_item(empty_set))