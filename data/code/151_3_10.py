def merge_dicts_by_key(list1, list2, key):
    result = {item[key]: item for item in list1}
    for item in list2:
        if item[key] in result:
            result[item[key]].update(item)
        else:
            result[item[key]] = item
    return [value for value in result.values()]

if __name__ == '__main__':
    list1 = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    list2 = [{'id': 2, 'age': 30}, {'id': 3, 'name': 'Charlie'}]
    merged_list = merge_dicts_by_key(list1, list2, 'id')
    print(merged_list)