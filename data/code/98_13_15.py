def filter_records(records):
    filtered = []
    for record in records:
        if (record['value'] > 10 and 
            record['status'] == 'active' and 
            isinstance(record['date'], str) and 
            len(record['date'].split('-')) == 3 and 
            all(part.isdigit() for part in record['date'].split('-'))):
            filtered.append(record)
    return filtered

if __name__ == '__main__':
    sample_records = [
        {'value': 15, 'status': 'active', 'date': '2023-10-05'},
        {'value': 8, 'status': 'inactive', 'date': '2023-10-06'},
        {'value': 12, 'status': 'active', 'date': '2023-10-07'}
    ]
    print(filter_records(sample_records))