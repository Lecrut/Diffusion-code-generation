def process_records(data):
    filtered_data = []
    for record in data:
        condition1 = record.get('value', 0) > 10
        condition2 = record.get('status') == 'active'
        condition3 = is_valid_date(record.get('date'))
        condition4 = record.get('category') in ['A', 'B', 'C']
        condition5 = record.get('amount', 0) > 50
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
        {'id': 1, 'value': 15, 'status': 'active', 'date': '2023-01-15', 'category': 'A', 'amount': 60},
        {'id': 2, 'value': 5, 'status': 'active', 'date': '2023-01-16', 'category': 'B', 'amount': 100},
        {'id': 3, 'value': 20, 'status': 'inactive', 'date': '2023-01-17', 'category': 'A', 'amount': 75},
        {'id': 4, 'value': 12, 'status': 'active', 'date': '2023/01/18', 'category': 'D', 'amount': 55},
        {'id': 5, 'value': 11, 'status': 'active', 'date': '2023-01-19', 'category': 'C', 'amount': 40},
        {'id': 6, 'value': 18, 'status': 'active', 'date': '2023-01-20', 'category': 'A', 'amount': 51},
    ]
    result = process_records(sample_data)
    print(result)