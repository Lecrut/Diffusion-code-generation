import json
def safe_get(data: dict | list, *keys) -> any:
    current = data
    for key in keys:
        if isinstance(current, (dict, list)):
            try:
                index_or_key = int(key) if isinstance(key, str) and key.isdigit() else key
                current = current[index_or_key]
            except (TypeError, ValueError):
                return None
        elif not isinstance(current, (dict, list)):
            return None
        else:
            return None
    return current
if __name__ == '__main__':
    sample_data = {
        "user": [
            {"id": 1},
            {"profile": {"age": 30}}
        ]
    }
    result_age = safe_get(sample_data, "user", 1, "profile", "age")
    print(result_age)