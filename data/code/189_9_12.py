def remove_all_occurrences(data_list, item_to_remove):
    if not isinstance(data_list, list) or not isinstance(item_to_remove, (int, str)):
        raise ValueError("Invalid input types. 'data_list' must be a list and 'item_to_remove' must be an int or str.")
    
    while item_to_remove in data_list:
        data_list.remove(item_to_remove)

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 30]
    item_to_remove = 30
    print("Original list:", my_list)
    remove_all_occurrences(my_list, item_to_remove)
    print("Resulting list:", my_list)