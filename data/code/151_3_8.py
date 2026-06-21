def merge_dicts_by_key(list1, list2, key):
    dict1 = {item[key]: item for item in list1}
    dict2 = {item[key]: item for item in list2}
    merged_dict = {**dict1, **dict2}
    return [merged_dict.get(k) for k in sorted(merged_dict.keys())]

if __name__ == '__main__':
    list1 = [{'id': 1, 'value': 'A'}, {'id': 3, 'value': 'C'}]
    list2 = [{'id': 2, 'value': 'B'}, {'id': 3, 'value': 'D'}]
    result = merge_dicts_by_key(list1, list2, 'id')
    print(result)