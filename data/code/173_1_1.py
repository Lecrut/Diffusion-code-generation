def group_data(data, key):
    grouped = {}
    for item in data:
        if key in item:
            group_value = item[key]
            if group_value not in grouped:
                grouped[group_value] = []
            grouped[group_value].append(item)
    return grouped
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'city': 'New York', 'age': 30},
        {'name': 'Bob', 'city': 'Los Angeles', 'age': 25},
        {'name': 'Charlie', 'city': 'New York', 'age': 35},
        {'name': 'David', 'city': 'Chicago', 'age': 28},
        {'name': 'Eve', 'city': 'Los Angeles', 'age': 22}
    ]
    grouping_key = 'city'
    result = group_data(sample_data, grouping_key)
    print(result)