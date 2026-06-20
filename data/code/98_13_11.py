def filter_records(records):
    filtered = []
    for record in records:
        if (record['value'] > 10 and 
            record['status'] == 'active' and 
            isinstance(record['date'], str) and 
            len(record['date']) == 10 and 
            record['date'].isdigit()):
            filtered.append(record)
    return filtered

if __name__ == '__main__':
    sample_records = [
        {'value': 15, 'status': 'active', 'date': '20230410'},
        {'value': 8, 'status': 'inactive', 'date': '20230410'},
        {'value': 15, 'status': 'active', 'date': '20230410'},
        {'value': 15, 'status': 'active', 'date': '20230410'}
    ]
    print(filter_records(sample_records))