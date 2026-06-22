def print_list_items(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be iterable")
    for item in iterable:
        print(item)

if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True]
    print_list_items(sample_list)