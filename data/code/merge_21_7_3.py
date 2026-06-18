def sort_objects_by_numerical_field(data):
    return sorted(data, key=lambda x: x['numerical_field'])
if __name__ == '__main__':
    data = [
        {'name': 'Alice', 'numerical_field': 30},
        {'name': 'Bob', 'numerical_field': 10},
        {'name': 'Charlie', 'numerical_field': 20},
        {'name': 'David', 'numerical_field': 5}
    ]
    sorted_data = sort_objects_by_numerical_field(data)
    for item in sorted_data:
        print(item)