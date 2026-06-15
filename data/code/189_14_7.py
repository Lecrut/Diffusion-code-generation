def remove_with_list_remove(data_list, item):
    try:
        data_list.remove(item)
    except ValueError:
        print(f"Error: Item '{item}' not found in the list.")
def remove_with_del(data_list, index):
    try:
        del data_list[index]
    except IndexError:
        print("Error: Index out of range.")
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    item_to_remove_remove = 30
    print("\nAttempting to remove", item_to_remove_remove, "using list.remove():")
    remove_with_list_remove(my_list, item_to_remove_remove)
    print("List after removing", item_to_remove_remove, ":", my_list)
    item_to_remove_error = 99
    print("\nAttempting to remove", item_to_remove_error, "using list.remove():")
    remove_with_list_remove(my_list, item_to_remove_error)
    print("List after failed removal:", my_list)
    index_to_remove = 1
    print("\nAttempting to remove element at index", index_to_remove, "using del:")
    remove_with_del(my_list, index_to_remove)
    print("List after deleting index", index_to_remove, ":", my_list)
    index_out_of_bounds = 100
    print("\nAttempting to delete element at index", index_out_of_bounds, "using del:")
    remove_with_del(my_list, index_out_of_bounds)
    print("List after failed deletion:", my_list)