def compare_dicts_by_key(list1, list2, key):
    differing_entries = []
    for dict1 in list1:
        matching_dict2 = next((d for d in list2 if d.get(key) == dict1.get(key)), None)
        if not matching_dict2 or dict1 != matching_dict2:
            differing_entries.append(dict1)
    return differing_entries

if __name__ == '__main__':
    sample_list1 = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    sample_list2 = [{'id': 1, 'name': 'Alicia'}, {'id': 3, 'name': 'Charlie'}]
    differing_entries = compare_dicts_by_key(sample_list1, sample_list2, 'id')
    print(differing_entries)