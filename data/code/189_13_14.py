def validate_input(lst, value):
    if not isinstance(lst, list) or not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Input must be a list of numbers")
    if not isinstance(value, (int, float)):
        raise ValueError("Value to remove must be a number")

def remove_item(original_list, item_to_remove):
    validate_input(original_list, item_to_remove)
    return [x for x in original_list if x != item_to_remove]

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 2, 5]
    item = 2
    new_list = remove_item(my_list, item)
    print(f"Original list: {my_list}")
    print(f"Item to remove: {item}")
    print(f"New list: {new_list}")