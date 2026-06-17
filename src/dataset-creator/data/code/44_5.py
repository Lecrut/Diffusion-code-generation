def search_dict(data, key):
    results = []
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                results.append(v)
            elif isinstance(v, (dict, list)):
                results.extend(search_dict(v, key))
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                results.extend(search_dict(item, key))
    return results
if __name__ == '__main__':
    sample_data = {
        "user": {"id": 123, "details": {"name": "Alice", "tags": ["admin"]}},
        "config": {"theme": "dark"},
        "items": [
            {"key": "target", "value": True},
            {"nested": {"search_key": False}}
        ]
    }
    target_keys = ["name", "id", "search_key"]
    for key in target_keys:
        found_values = search_dict(sample_data, key)
        print(f"Key '{key}' found at values: {found_values}")