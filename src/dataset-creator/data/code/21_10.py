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
        {'name': 'Alice', 'city': 'New York', 'age': 30},
        {'name': 'Bob', 'city': 'Los Angeles', 'age': 25},
        {'name': 'Charlie', 'city': 'New York', 'age': 35},
        {'name': 'David', 'city': 'Chicago', 'age': 28},
        {'name': 'Eve', 'city': 'Los Angeles', 'age': 22}
    ]
    grouping_key = 'city'
    organized_result = organize_data(sample_data, grouping_key)
    print(organized_result)