def remove_by_reference(data_list, item):
    if item in data_list:
        data_list.remove(item)
    else:
        print(f"Error: Item '{item}' not found in the list.")

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    item_to_remove = 30
    print("\nAttempting to remove", item_to_remove, "by reference:")
    remove_by_reference(my_list, item_to_remove)
    print("List after removal:", my_list)
    item_not_present = 99
    print("\nAttempting to remove", item_not_present, "by reference:")
    remove_by_reference(my_list, item_not_present)