def match_keys_to_values(keys_dict, values_dict):
    keys_set = set(keys_dict.keys())
    values_set = set(values_dict.keys())
    intersecting_keys = keys_set.intersection(values_set)
    result = {}
    for key in intersecting_keys:
        result[key] = keys_dict[key]
    return result
if __name__ == '__main__':
    keys_data = {'a': 1, 'b': 2, 'c': 3}
    values_data = {'b': 20, 'c': 30, 'd': 40}
    matched_data = match_keys_to_values(keys_data, values_data)
    print(matched_data)