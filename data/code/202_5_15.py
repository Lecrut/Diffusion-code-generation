def flatten_and_find_max(nested_list):
    return max(item for sublist in nested_list for item in (flatten_and_find_max(sublist) if isinstance(sublist, list) else [sublist]))

if __name__ == '__main__':
    sample = [[1, 2, [3]], 4, [5, [6, 7]]]
    print(flatten_and_find_max(sample))