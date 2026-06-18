import sys
def validate_and_retrieve(config: dict, keys_to_check: list) -> tuple[list[str], int]:
    if not isinstance(keys_to_check, list):
        raise TypeError("keys_to_check must be a list")
    missing_keys = []
    retrieved_values = []
    for key in keys_to_check:
        if key not in config:
            missing_keys.append(key)
        else:
            value = config[key]
            if isinstance(value, str):
                retrieved_values.append(f"{key}: {value}")
            elif isinstance(value, (int, float)):
                retrieved_values.append(f"{key}: {type(value).__name__}({value})")
    return missing_keys, len(retrieved_values)
if __name__ == '__main__':
    sample_config = {"username": "alice", "age": 30, "active": True}
    expected_keys = ["username", "email"]
    invalid_key_list, count_valid = validate_and_retrieve(sample_config, expected_keys)
    print("Missing keys:", invalid_key_list)
    print(f"Valid entries retrieved: {count_valid}")