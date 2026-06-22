def filter_records(records):
    results = []
    for record in records:
        value = record.get('value', 0)
        status = record.get('status', '')
        date_str = record.get('date', '')
        category = record.get('category', '')
        is_verified = record.get('is_verified', False)

        if value > 10:
            if status == 'active':
                if date_str and len(date_str) == 10:
                    if category in ['A', 'B', 'C']:
                        if is_verified:
                            results.append(record)
    return results

if __name__ == '__main__':
    sample_data = [
        {'value': 15, 'status': 'active', 'date': '2023-01-01', 'category': 'A', 'is_verified': True},
        {'value': 5, 'status': 'active', 'date': '2023-01-02', 'category': 'A', 'is_verified': True},
        {'value': 20, 'status': 'inactive', 'date': '2023-01-03', 'category': 'B', 'is_verified': True},
        {'value': 25, 'status': 'active', 'date': '2023-01-04', 'category': 'D', 'is_verified': True},
        {'value': 30, 'status': 'active', 'date': '2023-01-05', 'category': 'C', 'is_verified': False},
        {'value': 50, 'status': 'active', 'date': '2023-01-06', 'category': 'B', 'is_verified': True},
    ]
    filtered = filter_records(sample_data)
    print(filtered)