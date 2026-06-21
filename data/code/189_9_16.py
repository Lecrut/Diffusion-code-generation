def remove_all_occurrences(data_list, item_to_remove):
    start_index = len(data_list) - 1
    while start_index >= 0:
        if data_list[start_index] == item_to_remove:
            del data_list[start_index]
        start_index -= 1

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 30, 30]
    item_to_remove = 30
    print("Original list:", my_list)
    remove_all_occurrences(my_list, item_to_remove)
    print("Resulting list:", my_list)