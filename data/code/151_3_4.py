def merge_dicts_by_key(list1, list2, key):
    merged_dict = {item[key]: item for item in list1}
    for item in list2:
        if item[key] in merged_dict:
            merged_dict[item[key]].update(item)
        else:
            merged_dict[item[key]] = item
    return [value for value in merged_dict.values()]

if __name__ == '__main__':
    list1 = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'age': 30}]
    list2 = [{'id': 1, 'city': 'New York'}, {'id': 3, 'country': 'USA'}]
    result = merge_dicts_by_key(list1, list2, 'id')
    print(result)