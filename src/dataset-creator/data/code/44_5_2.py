import json
def search_dict(data: dict, target_key) -> list:
    results = []
    def traverse(current_data):
        if isinstance(current_data, dict):
            for key in current_data.keys():
                if key == target_key:
                    results.append(key)
                elif isinstance(current_data.get(key), (dict, list)):
                    traverse(current_data[key])
        elif isinstance(current_data, list):
            for item in current_data:
                if isinstance(item, dict):
                    traverse(item)
    traverse(data)
    return results
if __name__ == '__main__':
    sample = {
        "user": {"id": 123, "details": {}},
        "settings": ["key", "value"],
        "metadata": {
            "version": 1.0,
            "tags": [
                {"name": "alpha"},
                {"name": "beta"}
            ]
        }
    }
    target = "id"
    found_keys = search_dict(sample, target)
    print(f"Searched for key: {target}")
    print(f"Found keys at paths:")
    if not isinstance(found_keys[0], list):
        print(found_keys[0])
    else:
        print(", ".join(str(k) for k in found_keys))