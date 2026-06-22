def filter_records(records):
    valid_categories = {'A': True}
    result = []
    for record in records:
        value = record.get('value', 0)
        category = record.get('category', '')
        is_valid_category = valid_categories.get(category, False)
        condition_one = value > 100 and is_valid_category
        condition_two = value == 0
        if condition_one or condition_two:
            result.append(record)
    return result

if __name__ == '__main__':
    sample_data = [
        {'value': 150, 'category': 'A'},
        {'value': 50, 'category': 'A'},
        {'value': 200, 'category': 'B'},
        {'value': 0, 'category': 'A'},
        {'value': 100, 'category': 'A'},
        {'value': 101, 'category': 'B'},
        {'value': 0, 'category': 'B'},
        {'value': 101, 'category': 'A'}
    ]
    print(filter_records(sample_data))