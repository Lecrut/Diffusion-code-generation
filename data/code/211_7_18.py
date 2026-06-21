def compare_dicts(dict1, dict2):
    only_in_dict1 = {k: v for k, v in dict1.items() if k not in dict2}
    only_in_dict2 = {k: v for k, v in dict2.items() if k not in dict1}
    diff_values = {k: (dict1[k], dict2[k]) for k in set(dict1) & set(dict2) if dict1[k] != dict2[k]}
    return only_in_dict1, only_in_dict2, diff_values

if __name__ == '__main__':
    sample_dict1 = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
    sample_dict2 = {'banana': 'yellow', 'cherry': 'red', 'fig': 'green'}
    result = compare_dicts(sample_dict1, sample_dict2)
    print("Keys only in dict1:", result[0])
    print("Keys only in dict2:", result[1])
    print("Different values for common keys:", result[2])