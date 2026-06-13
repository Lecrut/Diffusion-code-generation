def safe_remove(data_list, item_to_remove):
    try:
        data_list.remove(item_to_remove)
    except ValueError as e:
        print(f"Error: Item '{item_to_remove}' not found in the list.")
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
    print(f"Success status: {success1}")
    print(f"List after first removal: {my_list}")
    print("\nAttempting to remove non-existing item:")
    success2 = safe_remove(my_list, item2)
    print(f"Success status: {success2}")
    print(f"List after second removal: {my_list}")
    my_list_empty = []
    print("\nAttempting to remove from an empty list:")
    success3 = safe_remove(my_list_empty, 10)
    print(f"Success status: {success3}")