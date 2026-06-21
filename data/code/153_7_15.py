def item_exists(nested_list, item):
    flattened = [x for sublist in nested_list for x in (sublist if isinstance(sublist, list) else [sublist])]
    return item in flattened
if __name__ == '__main__':
    sample_list = [[1, 2], [3, [4, 5]], 6]
    print(item_exists(sample_list, 5))
    print(item_exists(sample_list, 7))