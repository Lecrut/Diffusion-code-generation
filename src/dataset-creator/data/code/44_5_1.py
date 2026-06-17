def find_keys_in_dict(data_structure):
    keys_to_find = set()
    def _search(current_data):
        if isinstance(current_data, dict):
            for key in current_data.keys():
                if key in data_structure:                                                                                     
                    pass
            for key, value in current_data.items():
                keys_to_find.add(key)
        elif isinstance(current_data, list):
            for item in current_data:
                _search(item)
    def recursive_search(obj, target_keys_set):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in target_keys_set:
                    yield k
                else:
                    yield from recursive_search(v, target_keys_set)
        elif isinstance(obj, list):
            for item in obj:
                yield from recursive_search(item, target_keys_set)
    return set(k for k in recursive_search(data_structure, keys_to_find))
if __name__ == '__main__':
    sample_data = {
        "user": {"id": 123, "details": {"address": ["street", "city"]}},
        "config": {"theme": "dark"},
        "items": [{"key_a": True}, {"key_b": False}]
    }
    target_keys = ["id", "name", "nonexistent"]
    results = find_keys_in_dict(sample_data)
    print(f"Found keys: {results}")