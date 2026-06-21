def merge_dicts_by_key(list1, list2, key):
    dict1 = {item[key]: item for item in list1}
    dict2 = {item[key]: item for item in list2}
    merged_dict = {**dict1, **dict2}
    return [merged_dict[k] for k in sorted(merged_dict.keys())]

if __name__ == '__main__':
    sample_list1 = [{'id': 10, 'value': 'A'}, {'id': 20, 'value': 'B'}]
    sample_list2 = [{'id': 20, 'weight': 5}, {'id': 30, 'weight': 10}]
    merged_result = merge_dicts_by_key(sample_list1, sample_list2, 'id')
    print(merged_result)