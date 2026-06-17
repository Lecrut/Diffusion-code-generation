def print_list_items(iterable):
    for item in iterable:
        print(item)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print_list_items(sample_list)
    sample_tuple = ('a', 'b', 'c')
    print_list_items(sample_tuple)
    sample_string = "Hello"
    print_list_items(sample_string)