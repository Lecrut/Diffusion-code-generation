def get_first_item(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError('The input is not an iterable')
    try:
        return next(iter(iterable))
    except StopIteration:
        raise ValueError('The iterable is empty')

if __name__ == '__main__':
    sample_list = [100, 200, 300]
    sample_tuple = (400, 500, 600)
    sample_string = 'example'
    sample_set = {700, 800, 900}
    
    print(get_first_item(sample_list))
    print(get_first_item(sample_tuple))
    print(get_first_item(sample_string))
    print(get_first_item(sample_set))