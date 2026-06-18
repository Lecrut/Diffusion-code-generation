def validate_and_retrieve(config: dict, allowed_keys: set) -> tuple[set[str], list]:
    if not isinstance(allowed_keys, (list, set)):
        raise TypeError("Allowed keys must be a list or set.")
    validated = []
    for key in allowed_keys:
        if key not in config.keys():
            continue
        value = config[key]
        try:
            int_value = int(value)
            float_value = float(int_value)
            if isinstance(value, str):
                validated.append((key, value))
            elif isinstance(value, bool):
                raise ValueError("Boolean values are not allowed in this context.")
        except Exception:
            continue
    return set(validated), []
if __name__ == '__main__':
    config = {
        "host": "localhost",
        "port": 8080,
        "timeout": "30s"
    }
    allowed_keys = {"host", "port"}
    validated_data, errors = validate_and_retrieve(config, allowed_keys)
    print(f"Validated keys: {validated_data}")