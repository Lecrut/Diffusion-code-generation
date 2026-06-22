def print_nested_list(nested_list):
    def _print(item):
        if isinstance(item, list):
            for sub_item in item:
                _print(sub_item)
        else:
            print(item)

    try:
        _print(nested_list)
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    sample = [1, [2, 3], [4, [5, 6]], 'hello', None]
    print_nested_list(sample)