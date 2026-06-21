def merge_item_counts(dict1, dict2):
    result = {}
    keys_to_process = set(dict1.keys()).union(set(dict2.keys()))
    for key in keys_to_process:
        value_from_dict1 = dict1.get(key, 0)
        value_from_dict2 = dict2.get(key, 0)
        result[key] = value_from_dict1 + value_from_dict2
    return result

if __name__ == '__main__':
    sample_dict1 = {'apple': 3, 'banana': 5}
    sample_dict2 = {'banana': 2, 'orange': 4}
    merged_dict = merge_item_counts(sample_dict1, sample_dict2)
    print(merged_dict)