def get_first_item(iterable):
    def is_iterable(item):
        return hasattr(item, '__iter__')
    
    if not is_iterable(iterable):
        raise ValueError('The input is not an iterable')
    
    try:
        return next(iter(iterable))
    except StopIteration:
        raise ValueError('The iterable is empty')

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (40, 50, 60)
    sample_string = 'world'
    sample_set = {70, 80, 90}
    
    print(get_first_item(sample_list))
    print(get_first_item(sample_tuple))
    print(get_first_item(sample_string))
    print(get_first_item(sample_set))