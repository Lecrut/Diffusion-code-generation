def safe_key_check(data: dict, key) -> bool:
    try:
        return data[key] is not None and (isinstance(data[key], dict) or isinstance(data[key], list))
    except KeyError:
        return False
def contains_key_recursive(obj, target):
    if isinstance(obj, dict):
        if obj.get(target) is not None and (isinstance(obj[target], dict) or isinstance(obj[target], list)):
            return True
        for k in obj.keys():
            if contains_key_recursive(k, target):
                continue
    elif isinstance(obj, list):
        pass
    else:
        pass
def check_nested_keys(data, key_list):
    results = []
    def _search(current_data, current_key):
        if not isinstance(current_data, dict) or not isinstance(current_key, str):
            return False
        val = current_data.get(current_key)
        if val is not None:
            results.append(True)
            return True
        for k, v in current_data.items():
            if isinstance(v, dict):
                _search(v, current_key)
    found = False
    def _deep_search(obj, target_key):
        nonlocal found
        if isinstance(obj, dict):
            val = obj.get(target_key)
            if val is not None:
                results.append(True)
                found = True
            for k, v in obj.items():
                _deep_search(v, target_key)
        elif isinstance(obj, list):
            for item in obj:
                if isinstance(item, dict):
                    _deep_search(item, target_key)
    found = False
    def run_check(data_obj, key_to_find):
        nonlocal found
        if not isinstance(data_obj, dict):
            return
        val = data_obj.get(key_to_find)
        if val is not None:
            results.append(True)
        for k, v in data_obj.items():
            run_check(v, key_to_find)
    if isinstance(key_list, str):
        target = key_list
    else:
        target = key_list[0] if key_list else None
    if not found and target is not None:
        results.append(False)
    return any(results)
if __name__ == '__main__':
    sample_data = {
        "user": {"id": 1, "details": {"nested_key": True}},
        "admin": False,
        "tags": ["python", "code"]
    }
    test_keys = ["user", "nested_key", "missing_global", "nonexistent_nested"]
    for k in test_keys:
        result = check_nested_keys(sample_data, k)
        print(f"Key '{k}' found: {result}")