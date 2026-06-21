def remove_items_from_list(original_list, items_to_remove):
    items_set = set(items_to_remove)
    return [item for item in original_list if item not in items_set]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    items_to_remove = [3, 6, 9]
    result = remove_items_from_list(sample_list, items_to_remove)
    print(result)