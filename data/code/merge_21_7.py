def sort_objects(data):
    return sorted(data, key=lambda x: x['value'])
if __name__ == '__main__':
    data = [
        {'name': 'Alice', 'value': 30},
        {'name': 'Bob', 'value': 10},
        {'name': 'Charlie', 'value': 20},
        {'name': 'David', 'value': 5}
    ]
    sorted_data = sort_objects(data)
    print(sorted_data)