def remove_all_occurrences(data_list, item_to_remove):
    while item_to_remove in data_list:
        data_list.remove(item_to_remove)

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 30, 30]
    item_to_remove = 30
    print(f"Original list: {my_list}")
    remove_all_occurrences(my_list, item_to_remove)
    print(f"List after removing all occurrences of {item_to_remove}: {my_list}")