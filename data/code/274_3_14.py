def print_nested_list(nested_list):
    def _print_item(item):
        if isinstance(item, list):
            print_nested_list(item)
        else:
            print(item)

    for item in nested_list:
        _print_item(item)

if __name__ == '__main__':
    sample = [1, [2, 3], [4, [5, 6]], 7]
    print_nested_list(sample)