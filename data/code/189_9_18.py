def remove_all_occurrences(data_list, item_to_remove):
    i = len(data_list) - 1
    while i >= 0:
        if data_list[i] == item_to_remove:
            del data_list[i]
        i -= 1

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 30, 30]
    item_to_remove = 30
    print("Original list:", my_list)
    remove_all_occurrences(my_list, item_to_remove)
    print("Resulting list:", my_list)