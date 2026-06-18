def validate_and_retrieve(config: dict, keys_to_check) -> list:
    valid_values = []
    for key in keys_to_check:
        if key not in config:
            raise KeyError(f"Key '{key}' is missing from configuration.")
        value = config[key]
        if isinstance(value, str):
            try:
                int_val = int(value)
                float_val = float(value)
                valid_values.append((int_val, float_val))
            except ValueError as e:
                raise TypeError(f"Value for key '{key}' is not a valid number.") from e
        else:
            if isinstance(value, (list, tuple)):
                items_list = list(value)
                try:
                    int_items = [int(x) for x in items_list]
                    float_items = [float(x) for x in items_list]
                    valid_values.append((tuple(int_items), tuple(float_items)))
                except ValueError as e:
                    raise TypeError(f"Items in list/tuple for key '{key}' are not all numbers.") from e
            else:
                try:
                    int_val = int(value)
                    float_val = float(value)
                    valid_values.append((int_val, float_val))
                except ValueError as e:
                    raise TypeError(f"Value for non-list/non-tuple key '{key}' is not a number.") from e
    return valid_values
if __name__ == '__main__':
    sample_config = {
        "temperature": "25",
        "humidity": "60.5",
        "pressure_list": [1, 2, 3],
        "invalid_key": "not_a_number"
    }
    keys_to_check = ["temperature", "humidity"]
    try:
        result = validate_and_retrieve(sample_config, keys_to_check)
        print("Validation successful.")
        for item in result:
            print(f"{item}")
    except Exception as e:
        print(f"Error occurred: {e}")