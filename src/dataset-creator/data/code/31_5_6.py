def validate_and_retrieve(config: dict) -> tuple[list[str], list[dict]]:
    valid_keys = {'name', 'age'}
    result_values = []
    for key in config.keys():
        if key not in valid_keys:
            raise ValueError(f"Invalid key '{key}'. Expected one of {valid_keys}")
        value = config[key]
        if isinstance(value, dict):
            inner_valid_keys = {'location', 'status'}
            is_valid_inner = True
            for k, v in value.items():
                if k not in inner_valid_keys:
                    raise ValueError(f"Invalid nested key '{k}' under {key}. Expected one of {inner_valid_keys}")
                result_values.append({'name': config[key]['location'], 'status': config[key]['status']})
    return list(config.keys()), [{'value': v} for v in result_values]
if __name__ == '__main__':
    sample_config = {'age': 30, 'name': 'Alice', 'location': 'New York'}
    try:
        keys_list, values_data = validate_and_retrieve(sample_config)
        print(f"Validated Keys: {keys_list}")
        print("Retrieved Values:")
        for item in values_data:
            print(item['value'])
    except ValueError as e:
        print(str(e))