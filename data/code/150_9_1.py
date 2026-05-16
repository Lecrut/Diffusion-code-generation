def filter_list_of_dicts(data, key, value):
    filtered_list = [item for item in data if item.get(key) != value]
    return filtered_list
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'status': 'active'},
        {'id': 2, 'name': 'Bob', 'status': 'inactive'},
        {'id': 3, 'name': 'Charlie', 'status': 'active'},
        {'id': 4, 'name': 'David', 'status': 'inactive'}
    ]
    key_to_check = 'status'
    value_to_remove = 'active'
    result = filter_list_of_dicts(sample_data, key_to_check, value_to_remove)
    print(result)