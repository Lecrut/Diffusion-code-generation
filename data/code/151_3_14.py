def merge_lists_by_key(list1, list2, key):
    dict1 = {item[key]: item for item in list1}
    dict2 = {item[key]: item for item in list2}
    merged_dict = {**dict1, **dict2}
    return [merged_dict[k] for k in sorted(merged_dict.keys())]

if __name__ == '__main__':
    sample_list1 = [{'id': 1, 'name': 'Alice'}, {'id': 3, 'name': 'Charlie'}]
    sample_list2 = [{'id': 2, 'age': 25}, {'id': 3, 'age': 30}]
    merged_result = merge_lists_by_key(sample_list1, sample_list2, 'id')
    print(merged_result)