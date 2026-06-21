def filter_list(input_list, item_to_remove):
    if not isinstance(input_list, list) or not all(isinstance(item, (int, str)) for item in input_list):
        raise ValueError("Input must be a list of integers or strings")
    return [item for item in input_list if item != item_to_remove]

if __name__ == '__main__':
    try:
        original_list = [1, 2, '3', 4, 2, 5]
        item = 2
        new_list = filter_list(original_list, item)
        print(f"Original list: {original_list}")
        print(f"Item to remove: {item}")
        print(f"New list: {new_list}")
    except ValueError as e:
        print(e)