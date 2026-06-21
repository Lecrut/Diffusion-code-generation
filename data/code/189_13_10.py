def remove_item(original_list, item_to_remove):
    if not isinstance(original_list, list) or not isinstance(item_to_remove, (int, str)):
        raise ValueError("Invalid input. Expected a list and an integer or string.")
    
    return [x for x in original_list if x != item_to_remove]

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 2, 5]
    item = 2
    new_list = remove_item(my_list, item)
    print(f"Original list: {my_list}")
    print(f"Item to remove: {item}")
    print(f"New list: {new_list}")