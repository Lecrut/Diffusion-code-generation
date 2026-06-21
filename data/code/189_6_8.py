def remove_items(lst, items_to_remove):
    return list(set(lst) - set(items_to_remove))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    items_to_remove = [2, 4, 6, 8]
    result = remove_items(sample_list, items_to_remove)
    print(result)