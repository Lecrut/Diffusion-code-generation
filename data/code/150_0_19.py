def remove_item(lst, item_value):
    return [item for item in lst if item != item_value]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 6]
    item_to_remove = 3
    result = remove_item(sample_list, item_to_remove)
    print(result)