def merge_item_counts(dict1, dict2):
    result = {}
    for key in set(dict1) | set(dict2):
        result[key] = dict1.get(key, 0) + dict2.get(key, 0)
    return result

if __name__ == '__main__':
    sample_dict1 = {'apple': 3, 'banana': 5}
    sample_dict2 = {'banana': 2, 'orange': 4, 'grape': 6}
    merged_result = merge_item_counts(sample_dict1, sample_dict2)
    print(merged_result)