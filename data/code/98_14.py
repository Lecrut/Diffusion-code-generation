def process_records(data):
    filtered_data = []
    for record in data:
        condition1 = record.get('value', 0) > 10
        condition2 = record.get('status') == 'active'
        condition3 = is_valid_date(record.get('date'))
        condition4 = record.get('type') == 'A'
        condition5 = record.get('score', 0) >= 50
        if condition1 and condition2 and condition3 and condition4 and condition5:
            filtered_data.append(record)
    return filtered_data
def is_valid_date(date_str):
    try:
        import datetime
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except (ValueError, TypeError):
        return False
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 15, 'status': 'active', 'date': '2023-01-15', 'type': 'A', 'score': 60},
        {'id': 2, 'value': 5, 'status': 'active', 'date': '2023-01-16', 'type': 'B', 'score': 70},
        {'id': 3, 'value': 20, 'status': 'inactive', 'date': '2023-01-17', 'type': 'A', 'score': 80},
        {'id': 4, 'value': 12, 'status': 'active', 'date': '2023-02-18', 'type': 'A', 'score': 45},
        {'id': 5, 'value': 11, 'status': 'active', 'date': '2023-03-01', 'type': 'A', 'score': 55},
        {'id': 6, 'value': 18, 'status': 'active', 'date': '2023-04-01', 'type': 'C', 'score': 90}
    ]
    result = process_records(sample_data)
    print(result)