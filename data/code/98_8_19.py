def filter_records(records):
    result = []
    for record in records:
        value = record.get('value')
        category = record.get('category')
        if (value > 100 and category == 'A') or value == 0:
            result.append(record)
    return result

if __name__ == '__main__':
    sample_data = [
        {'value': 150, 'category': 'A'},
        {'value': 50, 'category': 'A'},
        {'value': 0, 'category': 'B'},
        {'value': 100, 'category': 'A'},
        {'value': 200, 'category': 'B'},
        {'value': 0, 'category': 'A'}
    ]
    filtered = filter_records(sample_data)
    print(filtered)