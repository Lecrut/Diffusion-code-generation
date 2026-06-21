def compare_dicts_by_key(list1, list2, key):
    differing_entries = []
    for item1, item2 in zip(list1, list2):
        if item1.get(key) != item2.get(key):
            differing_entries.append((item1, item2))
    return differing_entries

if __name__ == '__main__':
    sample_list_a = [{'id': 1, 'value': 'a'}, {'id': 2, 'value': 'b'}]
    sample_list_b = [{'id': 1, 'value': 'c'}, {'id': 2, 'value': 'd'}]
    result = compare_dicts_by_key(sample_list_a, sample_list_b, 'value')
    print(result)