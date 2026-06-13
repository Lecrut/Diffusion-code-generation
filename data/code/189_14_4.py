def remove_with_list_remove(data_list, item):
    try:
        data_list.remove(item)
    except ValueError:
        print(f"Error: Item '{item}' not found in the list.")
def remove_with_del(data_list, index):
    try:
        del data_list[index]
    except IndexError:
        print("Error: Index out of range for deletion.")
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    item_to_remove = 30
    print("\nAttempting to remove", item_to_remove, "using list.remove():")
    remove_with_list_remove(my_list, item_to_remove)
    print("List after removing", item_to_remove, ":", my_list)
    item_not_present = 99
    print("\nAttempting to remove", item_not_present, "using list.remove():")
    remove_with_list_remove(my_list, item_not_present)
    print("List after failed removal:", my_list)
    index_to_delete = 1
    print("\nAttempting to delete element at index", index_to_delete, "using del:")
    remove_with_del(my_list, index_to_delete)
    print("List after deleting index", index_to_delete, ":", my_list)
    invalid_index = 100
    print("\nAttempting to delete element at index", invalid_index, "using del:")
    remove_with_del(my_list, invalid_index)
    print("List after failed deletion:", my_list)