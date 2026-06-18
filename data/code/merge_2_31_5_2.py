import sys
def validate_and_retrieve(config: dict, keys_to_check: list) -> tuple[list[str], int]:
    invalid_keys = []
    retrieved_values = []
    for key in keys_to_check:
        if key not in config:
            invalid_keys.append(key)
        else:
            retrieved_values.append(config[key])
    return retrieved_values, len(invalid_keys)
if __name__ == '__main__':
    sample_config = {
        'database_host': 'localhost',
        'port_number': 5432,
        'timeout_seconds': 30
    }
    requested_keys = ['database_host', 'unknown_key']
    valid_values, invalid_count = validate_and_retrieve(sample_config, requested_keys)
    print(f"Retrieved values: {valid_values}")
    if invalid_count > 0:
        print(f"Invalid keys found ({invalid_count}): {[k for k in requested_keys if k not in sample_config]}")