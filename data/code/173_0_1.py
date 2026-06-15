def group_data(data_list, key):
    grouped = {}
    for item in data_list:
        if key in item:
            category = item[key]
            if category not in grouped:
                grouped[category] = []
            grouped[category].append(item)
    return grouped
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'city': 'New York', 'age': 30},
        {'name': 'Bob', 'city': 'Los Angeles', 'age': 25},
        {'name': 'Charlie', 'city': 'New York', 'age': 35},
        {'name': 'David', 'city': 'Chicago', 'age': 28},
        {'name': 'Eve', 'city': 'Los Angeles', 'age': 22}
    ]
    categorical_key = 'city'
    result = group_data(sample_data, categorical_key)
    print(result)