def print_nested_list(data):
    for item in data:
        if isinstance(item, list):
            print_nested_list(item)
        else:
            print(item)

if __name__ == '__main__':
    sample = [1, [2, 3], [4, [5, 6]], 7]
    print_nested_list(sample)