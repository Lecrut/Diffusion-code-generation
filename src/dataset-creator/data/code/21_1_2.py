def group_by_field(data, field):
    result = {}
    for item in data:
        key = item.get(field)
        if key is not None:
            if key not in result:
                result[key] = []
            result[key].append(item)
    return result
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'city': 'New York', 'age': 30},
        {'name': 'Bob', 'city': 'Los Angeles', 'age': 25},
        {'name': 'Charlie', 'city': 'New York', 'age': 35},
        {'name': 'David', 'city': 'Chicago', 'age': 28},
        {'name': 'Eve', 'city': 'Los Angeles', 'age': 22}
    ]
    field_to_group_by = 'city'
    grouped_data = group_by_field(sample_data, field_to_group_by)
    print(grouped_data)