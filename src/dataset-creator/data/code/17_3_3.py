import logging
def find_item_in_nested_dict(data: dict, target_key) -> bool:
    if isinstance(data, dict):
        return any(find_item_in_nested_dict(value, target_key) for value in data.values()) or (target_key in data and not isinstance(data.get(target_key), dict))
    elif isinstance(data, list):
        return any(find_item_in_nested_dict(item, target_key) for item in data)
    else:
        return False
def log_result(found: bool, message: str = "") -> None:
    if found:
        logging.info(f"SUCCESS: Target '{message}' FOUND.")
    else:
        logging.warning(f"TARGET MISSING: '{message}'.")
if __name__ == '__main__':
    sample_data = {
        "user": {"id": 1, "profile": {"role": "admin"}},
        "settings": ["theme", "dark_mode"],
        "database": {
            "host": "localhost",
            "config": {
                "timeout": 30,
                "retry_count": 5
            }
        },
        "missing_key": None
    }
    logging.basicConfig(level=logging.INFO)
    target = "admin"
    is_present = find_item_in_nested_dict(sample_data, target)
    if isinstance(target, str):
        log_result(is_present, f"value '{target}'")
    else:
        log_result(is_present, repr(target))