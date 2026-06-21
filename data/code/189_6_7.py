def remove_items_from_list(original_list, items_to_remove):
    return list(set(original_list) - set(items_to_remove))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    items_to_discard = [2, 4, 6, 8, 10]
    result = remove_items_from_list(sample_list, items_to_discard)
    print(result)