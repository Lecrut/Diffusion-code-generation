def filter_records(records):
    filtered = []
    for record in records:
        value = record.get('value', 0)
        category = record.get('category', '')
        condition = (value > 100 and category == 'A') or (value == 0)
        if condition:
            filtered.append(record)
    return filtered
if __name__ == '__main__':
    sample_data = [
        {'value': 150, 'category': 'A'},
        {'value': 50, 'category': 'A'},
        {'value': 200, 'category': 'B'},
        {'value': 0, 'category': 'A'},
        {'value': 100, 'category': 'A'},
        {'value': 101, 'category': 'B'},
        {'value': 0, 'category': 'B'},
        {'value': 100, 'category': 'B'}
    ]
    result = filter_records(sample_data)
    print(result)