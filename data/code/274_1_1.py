def print_list_items(iterable):
    for item in iterable:
        print(item)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'a', 4.5]
    print_list_items(sample_list)
    sample_tuple = ('hello', 'world')
    print_list_items(sample_tuple)