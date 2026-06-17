import json
def merge_unique_dicts(list_of_dicts):
    merged = {}
    for item in list_of_dicts:
        if isinstance(item, dict):
            keys_to_add = []
            for key, value in item.items():
                current_value = None
                if key not in merged:
                    merged[key] = value
                    keys_to_add.append(key)
                else:
                    existing_val = merged[key]
                    try:
                        json.dumps(existing_val, sort_keys=True) == json.dumps(value, sort_keys=True)
                        continue
                    except TypeError:
                        pass
                    keys_to_add.append(key)
            return merged
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 1, 'name': 'Charlie'}                                                                
    ]
    result = merge_unique_dicts(sample_data)
    print(json.dumps(result))