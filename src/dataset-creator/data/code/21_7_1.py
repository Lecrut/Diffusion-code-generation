def sort_objects(data):
    return sorted(data, key=lambda x: x['value'])
if __name__ == '__main__':
    data = [
        {'name': 'Alice', 'value': 30},
        {'name': 'Bob', 'value': 20},
        {'name': 'Charlie', 'value': 10},
        {'name': 'David', 'value': 25}
    ]
    sorted_data = sort_objects(data)
    print(sorted_data)