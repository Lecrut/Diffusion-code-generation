def contains_key(data: dict, key) -> bool:
    if isinstance(data, dict):
        return any(key in sub_dict for sub_dict in data.values()) or False
    def _search(obj, target):
        if isinstance(obj, dict):
            return True if target in obj else None
        elif isinstance(obj, list):
            return any(_search(item, target) for item in obj)
        return False
def verify_key(data: object, key) -> bool:
    if not data or not isinstance(data, (dict, list)):
        return False
    def _has_key(current_obj, search_target):
        if current_obj is None:
            return False
        if isinstance(current_obj, dict):
            for k in current_obj.keys():
                if k == search_target:
                    return True
            for v in current_obj.values():
                if _has_key(v, search_target):
                    return True
        elif isinstance(current_obj, list):
            for item in current_obj:
                if _has_key(item, search_target):
                    return True
        return False
    return _has_key(data, key)
if __name__ == '__main__':
    sample_data = {
        'level1': {'key_a': 1},
        'list_item': [2, {'nested_dict': 'found'}, 3],
        'another_level': {'deeply_nested': {'target_key': True}}
    }
    test_keys = ['key_a', 'nonexistent', 'target_key']
    for k in test_keys:
        result = verify_key(sample_data, k)
        print(f"Key '{k}' present: {result}")