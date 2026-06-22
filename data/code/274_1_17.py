def print_items(iterable):
    if not isinstance(iterable, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    for item in iterable:
        print(item)

if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True]
    print_items(sample_list)