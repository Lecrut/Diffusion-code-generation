def filter_records(records):
    filtered = []
    for record in records:
        if (record['value'] > 10 
            and record['status'] == 'active' 
            and isinstance(record['date'], str) 
            and len(record['date']) == 10 
            and record['date'].replace('-', '').isdigit()):
            filtered.append(record)
    return filtered

if __name__ == '__main__':
    sample_records = [
        {'value': 5, 'status': 'active', 'date': '2023-04-30'},
        {'value': 15, 'status': 'inactive', 'date': '2023-04-30'},
        {'value': 20, 'status': 'active', 'date': '2023-04-30'},
        {'value': 10, 'status': 'active', 'date': '2023-04-30'}
    ]
    print(filter_records(sample_records))