def subtract_dictionaries(dict1, dict2):
    result = {}
    keys_to_check = set(dict1).union(set(dict2))
    for key in keys_to_check:
        count1 = dict1.get(key, 0)
        count2 = dict2.get(key, 0)
        result[key] = count1 - count2
    return result

if __name__ == '__main__':
    sample_dict1 = {'apple': 4, 'banana': 6, 'cherry': 3}
    sample_dict2 = {'banana': 3, 'cherry': 5, 'date': 8}
    print(subtract_dictionaries(sample_dict1, sample_dict2))