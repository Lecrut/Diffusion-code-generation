def print_list_items(iterable):
    for item in iterable:
        print(item)
if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True, [5, 6]]
    print_list_items(sample_list)