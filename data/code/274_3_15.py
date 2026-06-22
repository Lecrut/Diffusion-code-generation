def print_nested_list(nested_list):
    def _print_item(item):
        if isinstance(item, list):
            _print_list(item)
        else:
            print(item)

    def _print_list(lst):
        for item in lst:
            _print_item(item)

    try:
        _print_list(nested_list)
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    sample = [1, [2, 3], [4, [5, 6]], 7]
    print_nested_list(sample)