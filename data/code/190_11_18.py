def check_item_in_list(item_list, target):
    if not isinstance(item_list, list) or not all(isinstance(item, (int, float, str)) for item in item_list):
        raise ValueError("item_list must be a list of integers, floats, or strings")
    return target in item_list

if __name__ == '__main__':
    sample_items = [10, 25, "apple", 42.0]
    target_item = 42.0
    try:
        result = check_item_in_list(sample_items, target_item)
        if result:
            print(f"The item {target_item} exists in the list.")
        else:
            print(f"The item {target_item} does not exist in the list.")
    except ValueError as e:
        print(e)