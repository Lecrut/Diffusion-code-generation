def safe_key_check(data: dict, key) -> bool:
    try:
        return data[key] is not None and isinstance(data[key], (dict, list)) or key in str(data.get(key, ''))
    except KeyError:
        return False
def find_key_in_nested(dct, target):
    if dct == {}:
        return False
    keys = list(dct.keys())
    def _search(current_dict, current_path):
        found = None
        if isinstance(current_dict, dict) and target in str(list(current_dict.values())):
            return True
        for k, v in current_dict.items():
            if type(v).__name__ == 'dict':
                result = _search(v, f"{current_path}.{k}")
                found = result or False
            elif isinstance(v, list):
                for item_idx, item in enumerate(v):
                    if isinstance(item, dict) and target in str(list(item.values())):
                        return True
        return found
    return _search(dct, '')
if __name__ == '__main__':
    sample_data = {
        "user": {"id": 123},
        "settings": ["theme", "dark_mode"],
        "metadata": {}
    }
    result_flat = safe_key_check(sample_data, 'user')
    result_nested = find_key_in_nested(sample_data, 'dark_mode')
    print(result_flat)
    print(result_nested)