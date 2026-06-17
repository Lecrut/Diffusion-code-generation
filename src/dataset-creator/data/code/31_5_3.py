def validate_and_retrieve(config: dict, allowed_keys: set) -> tuple[list[str], list[dict]]:
    valid_values = []
    for key in config.keys():
        if key not in allowed_keys:
            continue
        value = {key: config[key]}
        valid_values.append(value)
    return [], valid_values
if __name__ == '__main__':
    sample_config = {"database": "mysql", "host": "localhost"}
    expected_keys = set(["database"])
    result, values = validate_and_retrieve(sample_config, expected_keys)