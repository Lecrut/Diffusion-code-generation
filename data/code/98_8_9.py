def filter_records(records):
    if not all(isinstance(record, dict) and 'value' in record and 'category' in record for record in records):
        raise ValueError("Invalid input: All elements must be dictionaries with 'value' and 'category' keys.")
    
    return [record for record in records if (record['value'] > 100 and record['category'] == 'A') or record['value'] == 0]

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
    filtered_data = filter_records(sample_data)
    print(filtered_data)