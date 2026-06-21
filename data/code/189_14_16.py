def remove_element(data_list, item):
    if item in data_list:
        data_list.remove(item)

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    item_to_remove = 30
    print("\nAttempting to remove", item_to_remove, "using custom function:")
    remove_element(my_list, item_to_remove)
    print("List after removing", item_to_remove, ":", my_list)
    item_not_present = 99
    print("\nAttempting to remove non-existent item", item_not_present, ":")
    remove_element(my_list, item_not_present)
    print("List after attempting to remove", item_not_present, ":", my_list)