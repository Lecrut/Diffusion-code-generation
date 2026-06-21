def remove_items(lst, items_to_remove):
    items_set = set(items_to_remove)
    return [item for item in lst if item not in items_set]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    items_to_remove = [2, 4, 6, 8]
    result = remove_items(sample_list, items_to_remove)
    print(result)