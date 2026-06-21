def validate_input(input_list, item_to_remove):
    if not isinstance(input_list, list):
        raise ValueError("input_list must be a list")
    if not any(isinstance(item, (int, float)) for item in input_list):
        raise ValueError("All elements in input_list must be numbers")
    if not isinstance(item_to_remove, (int, float)):
        raise ValueError("item_to_remove must be a number")

def remove_item_from_list(input_list, item_to_remove):
    validate_input(input_list, item_to_remove)
    return [item for item in input_list if item != item_to_remove]

if __name__ == '__main__':
    original_list = [1, 2, 3, 4, 2, 5]
    item = 2
    new_list = remove_item_from_list(original_list, item)
    print(f"Original list: {original_list}")
    print(f"Item to remove: {item}")
    print(f"New list: {new_list}")