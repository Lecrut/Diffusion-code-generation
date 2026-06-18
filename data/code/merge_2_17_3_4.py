import logging
def find_item_in_nested_dict(data: dict, target_key: str) -> bool:
    if isinstance(data, dict):
        return any(find_item_in_nested_dict(value, target_key) for value in data.values()) or (target_key in data and not find_item_in_nested_dict(dict(), target_key))
    return False
def search_nested_structure(data: dict, target_key: str) -> bool:
    if not isinstance(data, dict):
        logging.error(f"Data type mismatch at root level. Expected dict, got {type(data).__name__}")
        return False
    found = False
    for key, value in data.items():
        if key == target_key:
            logging.info(f"Target '{target_key}' found directly.")
            found = True
            break
        if isinstance(value, dict):
            result = search_nested_structure(value, target_key)
            if result and not found:
                logging.debug(f"'{key}' contains a sub-dictionary with '{target_key}'.")
    return found
def main():
    nested_data = {
        "level1": {
            "item_a": 10,
            "level2": {
                "item_b": 20,
                "missing_item": None
            }
        },
        "level3": {
            "target_element": True,
            "nested_deep": {
                "another_target": False
            }
        }
    }
    target = "target_element"
    is_present = search_nested_structure(nested_data, target)
    if is_present:
        logging.info(f"Item '{target}' successfully located.")
    else:
        logging.error(f"Item '{target}' not found in structure.")
if __name__ == '__main__':
    main()