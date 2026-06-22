def get_first_item(iterable):
    if not iterable:
        raise ValueError('The iterable is empty')
    return next(iter(iterable))
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30)
    sample_string = 'hello'
    print(get_first_item(sample_list))
    print(get_first_item(sample_tuple))
    print(get_first_item(sample_string))