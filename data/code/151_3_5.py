def merge_dicts_by_key(list1, list2, key):
    merged_dict = {item[key]: item for item in list1}
    for item in list2:
        if item[key] in merged_dict:
            merged_dict[item[key]].update(item)
        else:
            merged_dict[item[key]] = item
    return list(merged_dict.values())

if __name__ == '__main__':
    sample_list1 = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    sample_list2 = [{'id': 2, 'age': 30}, {'id': 3, 'name': 'Charlie'}]
    merged_result = merge_dicts_by_key(sample_list1, sample_list2, 'id')
    print(merged_result)