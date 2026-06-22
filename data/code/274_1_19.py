def print_list_items(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")
    for item in iterable:
        print(item)

if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True]
    try:
        print_list_items(sample_list)
    except ValueError as e:
        print(e)
    
    sample_tuple = ('a', 'b', 'c')
    try:
        print_list_items(sample_tuple)
    except ValueError as e:
        print(e)