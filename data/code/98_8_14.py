def filter_records(records):
    return [record for record in records if (record['value'] > 100 and record['category'] == 'A') or record['value'] == 0]

if __name__ == '__main__':
    sample_records = [
        {'value': 50, 'category': 'A'},
        {'value': 150, 'category': 'B'},
        {'value': 0, 'category': 'A'},
        {'value': 200, 'category': 'A'}
    ]
    filtered_records = filter_records(sample_records)
    print(filtered_records)