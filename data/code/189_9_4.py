def safe_remove(data_list, item_to_remove):
    try:
        data_list.remove(item_to_remove)
    except ValueError as e:
        print(f"Error: Could not remove '{item_to_remove}'. Item not found in the list.")
        return False
    return True
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    item1 = 30
    item2 = 99
    print("Original list:", my_list)
    print("\nAttempting to remove existing item (", item1, "):")
    success1 = safe_remove(my_list, item1)
    print("List after attempt 1:", my_list)
    print("\nAttempting to remove non-existing item (", item2, "):")
    success2 = safe_remove(my_list, item2)
    print("List after attempt 2:", my_list)
    print("\nFinal list:", my_list)