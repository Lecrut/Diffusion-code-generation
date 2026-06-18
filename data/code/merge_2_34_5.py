def merge_unique_dicts(list_of_dicts):
    merged = {}
    for item in list_of_dicts:
        if isinstance(item, dict) and not any(isinstance(v, (list, set)) for v in item.values()):
            keys_to_add = [k for k in item.keys() if k not in merged]
            for key in keys_to_add:
                merged[key] = item[key]
    return merged
if __name__ == '__main__':
    sample_data = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5}]
    result = merge_unique_dicts(sample_data)
    print(result)