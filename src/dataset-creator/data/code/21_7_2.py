def sort_objects_by_number(data):
    return sorted(data, key=lambda x: x['value'])
if __name__ == '__main__':
    data = [
        {'name': 'Apple', 'value': 5},
        {'name': 'Banana', 'value': 2},
        {'name': 'Cherry', 'value': 8},
        {'name': 'Date', 'value': 1},
        {'name': 'Elderberry', 'value': 4}
    ]
    sorted_data = sort_objects_by_number(data)
    for item in sorted_data:
        print(item)