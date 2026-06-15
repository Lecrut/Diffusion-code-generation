def match_keys_to_values(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            result[key] = dict1[key]
    return result
if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict_b = {'a': 1, 'b': 99, 'c': 3, 'e': 5}
    matched_data = match_keys_to_values(dict_a, dict_b)
    print(matched_data)