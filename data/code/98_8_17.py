THRESHOLD = 100
CATEGORY_A = 'A'

def filter_records(records):
    filtered = []
    for record in records:
        value = record.get('value', 0)
        category = record.get('category', '')
        if (value > THRESHOLD and category == CATEGORY_A) or (value == 0):
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
        {'value': 0, 'category': 'B'}
    ]
    print(filter_records(sample_data))