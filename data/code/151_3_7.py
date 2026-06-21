def merge_dicts_by_key(list1, list2, key):
    merged = {d[key]: d for d in list1}
    for d in list2:
        if d[key] in merged:
            merged[d[key]].update(d)
        else:
            merged[d[key]] = d
    return [v for v in merged.values()]

if __name__ == '__main__':
    sample_list1 = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    sample_list2 = [{'id': 2, 'age': 30}, {'id': 3, 'name': 'Charlie'}]
    result = merge_dicts_by_key(sample_list1, sample_list2, 'id')
    print(result)