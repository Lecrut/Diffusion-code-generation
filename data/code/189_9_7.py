def safe_remove(data_list, item_to_remove):
    if item_to_remove in data_list:
        try:
            data_list.remove(item_to_remove)
        except ValueError:
            raise IndexError("Attempted to remove an item that was not found in the list.")
    else:
        raise IndexError(f"Item '{item_to_remove}' not found in the list for removal.")
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    item_to_remove_success = 3
    item_to_remove_not_found = 99
    print(f"Original list: {my_list}")
    try:
        safe_remove(my_list, item_to_remove_success)
        print(f"Successfully removed {item_to_remove_success}. List after success: {my_list}")
        safe_remove(my_list, item_to_remove_not_found)
    except IndexError as e:
        print(f"Caught expected error for missing item: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print(f"Final list state: {my_list}")