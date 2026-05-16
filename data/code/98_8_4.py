def filter_records(data):
    filtered_list = []
    for record in data:
        value = record.get('value', 0)
        category = record.get('category', '')
        condition = (value > 100 and category == 'A') or (value == 0)
        if condition:
            filtered_list.append(record)
    return filtered_list
if __name__ == '__main__':
    sample_data = [
        {'value': 150, 'category': 'A'},
        {'value': 50, 'category': 'A'},
        {'value': 200, 'category': 'B'},
        {'value': 0, 'category': 'A'},
        {'value': 100, 'category': 'A'},
        {'value': 120, 'category': 'B'},
        {'value': 0, 'category': 'B'},
        {'value': 101, 'category': 'A'}
    ]
    result = filter_records(sample_data)
    print(result)