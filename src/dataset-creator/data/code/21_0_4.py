def organize_objects(data, key, value):
    grouped_data = {}
    for obj in data:
        if key in obj and obj[key] == value:
            if value not in grouped_data:
                grouped_data[value] = []
            grouped_data[value].append(obj)
    return grouped_data
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'city': 'New York', 'age': 30},
        {'name': 'Bob', 'city': 'Los Angeles', 'age': 25},
        {'name': 'Charlie', 'city': 'New York', 'age': 35},
        {'name': 'David', 'city': 'Chicago', 'age': 25},
        {'name': 'Eve', 'city': 'Los Angeles', 'age': 30}
    ]
    grouping_key = 'city'
    grouping_value = 'New York'
    organized_result = organize_objects(sample_data, grouping_key, grouping_value)
    print(organized_result)