def print_nested_list(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            print_nested_list(item)
        else:
            print(item)

if __name__ == '__main__':
    sample = [1, [2, 3], [4, [5, 6]]]
    print_nested_list(sample)