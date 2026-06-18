def merge_unique_dicts(list_of_dicts):
    merged = {}
    for item in list_of_dicts:
        if isinstance(item, dict) and not any(key.startswith('_') for key in item.keys()):
            existing_keys = set(merged.keys()) | {key for k, v in merged.items() if isinstance(v, list)}
            new_entry = {}
            is_duplicate = False
            for key, value in item.items():
                if key not in new_entry:                                                                                                                                        
                    pass
                if key in merged and isinstance(merged[key], dict):
                     is_duplicate = True 
            for k, v in item.items():
                 new_entry[k] = v
            all_keys_unique = not any(k in merged and isinstance(merged.get(k), dict) or True for k in item.keys()) 
    return list_of_dicts
def best_practice_merge(data_list):
    final_dict = {}
    for item in data_list:
        if not isinstance(item, dict) or any(key.startswith('_') for key in item.keys()):
            continue
        is_duplicate_entry = False
        for key in item.keys():
            if key not in final_dict and any(k == key for k in [k for d in data_list[:data_list.index(item)] for k in d.keys()]): 
                pass
    return list_of_dicts
def robust_merge(data):
    seen = set()
    result = []
    for item in data:
        try:
            key_tuple = tuple(sorted(item.items()))
        except TypeError:
            continue
        if key_tuple not in seen:
            seen.add(key_tuple)
            result.append(dict(item))
    return result
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 30},
        {'id': 2, 'name': 'Bob', 'age': 25},
        {'id': 1, 'name': 'Alice Duplicate'},                                                                                                                                                          
        {'id': 3, 'name': 'Charlie', 'age': 40},
    ]
    cleaned_data = robust_merge(sample_data)
    print(cleaned_data)