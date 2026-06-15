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
    item_to_remove_remove = 30
    print("\nAttempting to remove", item_to_remove_remove, "using list.remove():")
    remove_with_list_remove(my_list, item_to_remove_remove)
    print("List after using list.remove():", my_list)
    item_not_present = 99
    print("\nAttempting to remove", item_not_present, "using list.remove():")
    remove_with_list_remove(my_list, item_not_present)
    print("List after failed removal attempt:", my_list)
    index_to_remove_del = 1
    print("\nAttempting to remove element at index", index_to_remove_del, "using del:")
    remove_with_del(my_list, index_to_remove_del)
    print("List after using del:", my_list)
    index_out_of_bounds = 100
    print("\nAttempting to remove element at index", index_out_of_bounds, "using del:")
    remove_with_del(my_list, index_out_of_bounds)
    print("List after failed deletion attempt:", my_list)