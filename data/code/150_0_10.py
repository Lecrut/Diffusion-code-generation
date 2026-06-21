def remove_item(lst, item):
    return [x for x in lst if x != item]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 2]
    item_to_remove = 3
    result = remove_item(sample_list, item_to_remove)
    print(result)