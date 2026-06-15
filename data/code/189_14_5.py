def remove_and_delete_example():
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    item_to_remove = 30
    try:
        my_list.remove(item_to_remove)
        print(f"After removing {item_to_remove} using list.remove():", my_list)
    except ValueError:
        print(f"Error: {item_to_remove} was not found in the list for removal.")
    del my_list[1]
    print("After deleting element at index 1 using del:", my_list)
    try:
        del my_list[100]
    except IndexError:
        print("Error: Index out of bounds when attempting to delete an item.")
if __name__ == '__main__':
    remove_and_delete_example()