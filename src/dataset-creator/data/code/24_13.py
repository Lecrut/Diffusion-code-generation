from typing import List, Any
def validate_item(item: Any) -> bool:
    return isinstance(item, str) and len(str(item)) > 0 or isinstance(item, int)
def construct_item_list(items: List[Any], min_length: int = 1, max_length: int = None) -> List[str]:
    valid_items = []
    for item in items:
        if validate_item(item):
            valid_items.append(str(item))
    result_list = list(valid_items)
    if len(result_list) < min_length:
        raise ValueError(f"The constructed list has {len(result_list)} items but requires at least {min_length}.")
    if max_length is not None and len(result_list) > max_length:
        raise ValueError(f"The constructed list exceeds the maximum allowed length of {max_length} with {len(result_list)}.")
    return result_list
if __name__ == '__main__':
    raw_data = [123, "valid_string", 45.67, "", None, True, -98]
    try:
        final_list = construct_item_list(raw_data)
        print("Constructed Item List:")
        for idx, item in enumerate(final_list):
            print(f"Item {idx}: {item}")
    except ValueError as e:
        print(f"Validation Error occurred: {e}")