def remove_item(lst, item):
    return [x for x in lst if x != item]
if __name__ == '__main__':
    original_list = [1, 2, 3, 4, 5, 2, 6]
    item_to_remove = 2
    new_list = remove_item(original_list, item_to_remove)
    print(new_list)