def get_first_item(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError('The iterable is empty')

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        (4, 5, 6),
        'abc',
        {7, 8, 9},
        range(10, 15)
    ]
    
    for item in sample_data:
        print(get_first_item(item))