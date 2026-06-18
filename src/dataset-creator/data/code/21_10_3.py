def organize_data(data_list, group_by_key):
    organized_data = {}
    for item in data_list:
        key = item.get(group_by_key)
        if key is not None:
            if key not in organized_data:
                organized_data[key] = []
            organized_data[key].append(item)
    return organized_data
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 35, 'city': 'New York'},
        {'name': 'David', 'age': 28, 'city': 'Chicago'}
    ]
    grouping_key = 'city'
    organized_result = organize_data(sample_data, grouping_key)
    print(organized_result)