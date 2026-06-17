def print_items_separately(iterable):
    for item in iterable:
        print(item)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = ('a', 'b', 'c', 'd')
    print("Printing list items separately:")
    print_items_separately(sample_list)
    print("\nPrinting tuple items separately:")
    print_items_separately(sample_tuple)