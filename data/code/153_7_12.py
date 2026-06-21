def item_exists(nested_list, target):
    flattened = [item for sublist in nested_list for item in (sublist if isinstance(sublist, list) else [sublist])]
    return target in flattened
if __name__ == '__main__':
    sample_list = [[1, 2], [3, 4], [5, [6, 7]]]
    print(item_exists(sample_list, 5))
    print(item_exists(sample_list, 8))