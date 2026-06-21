def remove_element_by_reference(data_list, item):
    try:
        index = data_list.index(item)
        del data_list[index]
    except ValueError:
        print(f"Error: Item '{item}' not found in the list.")

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    item_to_remove = 30
    print("\nAttempting to remove", item_to_remove, "by reference:")
    remove_element_by_reference(my_list, item_to_remove)
    print("List after removing", item_to_remove, ":", my_list)
    item_not_present = 99