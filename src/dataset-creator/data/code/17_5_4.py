import json
def check_item_existence(data: object, target_value) -> bool:
    def _recursive_check(obj):
        if obj == target_value:
            return True
        if isinstance(obj, (dict, list)):
            for item in obj.values() if isinstance(obj, dict) else obj:
                if _recursive_check(item):
                    return True
        elif isinstance(obj, tuple):
            for item in obj:
                if _recursive_check(item):
                    return True
        elif isinstance(obj, set):
            for item in obj:
                if _recursive_check(item):
                    return True
        elif isinstance(obj, list):
            for item in obj:
                if _recursive_check(item):
                    return True
        return False
    try:
        result = _recursive_check(data)
        return bool(result)
    except Exception:
        return data == target_value
if __name__ == '__main__':
    sample_data = {
        "users": [
            {"id": 1, "name": "Alice", "address": {"city": "New York"}},
            {"id": 2, "name": "Bob", "tags": ["admin", "guest"]}
        ],
        "metadata": {
            "version": 1.0,
            "status": True
        }
    }
    test_cases = [
        ("Alice", sample_data),
        ({"id": 2}, sample_data),
        ({"city": "New York"}, sample_data),
        ([], sample_data),                                                                              
        ((1, 2), sample_data)
    ]
    for value, data in test_cases:
        exists = check_item_existence(data, value)
        print(f"Checking {value} in data: {exists}")