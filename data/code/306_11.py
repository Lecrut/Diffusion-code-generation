def print_list_items(iterable):
    for item in iterable:
        print(item)
if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True]
    print("--- Printing list items ---")
    print_list_items(sample_list)
    sample_tuple = ('a', 'b', 'c')
    print("\n--- Printing tuple items ---")
    print_list_items(sample_tuple)