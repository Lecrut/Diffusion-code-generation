def match_keys_to_values(keys_dict, values_dict):
    keys = set(keys_dict.keys())
    values = set(values_dict.keys())
    intersecting_keys = keys.intersection(values)
    result = {}
    for key in intersecting_keys:
        result[key] = keys_dict[key]
    return result
if __name__ == '__main__':
    keys_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    values_data = {'b': 20, 'c': 30, 'e': 50, 'a': 10}
    matched_data = match_keys_to_values(keys_data, values_data)
    print(matched_data)