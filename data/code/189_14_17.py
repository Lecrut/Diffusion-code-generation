def validate_index(data_list, index):
    if not isinstance(index, int) or index < 0 or index >= len(data_list):
        raise IndexError("Index out of range for deletion.")

def remove_by_reference(data_list, item):
    try:
        data_list.remove(item)
    except ValueError:
        print(f"Error: Item '{item}' not found in the list.")

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    
    item_to_remove = 30
    try:
        validate_index(my_list, my_list.index(item_to_remove))
        remove_by_reference(my_list, item_to_remove)
        print("Item removed successfully.")
    except ValueError as e:
        print(e)

    print("List after removal:", my_list)