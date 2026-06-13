def safe_remove(data_list, item_to_remove):
    try:
        data_list.remove(item_to_remove)
    except ValueError as e:
        print(f"Error: Item not found in the list. {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    return True
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    item1 = 30
    item2 = 99
    print(f"Original list: {my_list}")
    print("\nAttempting to remove existing item:")
    success1 = safe_remove(my_list, item1)
    print(f"Success: {success1}, Current list: {my_list}")
    print("\nAttempting to remove non-existing item (Boundary Error):")
    success2 = safe_remove(my_list, item2)
    print(f"Success: {success2}, Current list: {my_list}")
    print("\nAttempting to remove an item that might be duplicated (demonstrating behavior):")
    my_list_dup = [10, 20, 30, 30, 50]
    item3 = 30
    success3 = safe_remove(my_list_dup, item3)
    print(f"Success: {success3}, Current list: {my_list_dup}")
    print("\nFinal list state:")
    print(my_list)
    print(my_list_dup)