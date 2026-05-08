def remove_item_from_list(input_list, item_to_remove):
    new_list = [item for item in input_list if item != item_to_remove]
    return new_list
if __name__ == '__main__':
    original_list = [1, 2, 3, 4, 2, 5]
    item = 2
    new_list = remove_item_from_list(original_list, item)
    print(f"Original list: {original_list}")
    print(f"Item to remove: {item}")
    print(f"New list: {new_list}")