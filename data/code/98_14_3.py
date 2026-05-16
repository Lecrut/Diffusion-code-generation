def process_records(data):
    filtered_list = []
    for record in data:
        condition1 = record.get('value', 0) > 10
        condition2 = record.get('status') == 'active'
        condition3 = '2023-01-01' <= record.get('date', 'invalid_date') <= '2024-12-31'
        condition4 = isinstance(record.get('id'), int)
        condition5 = record.get('amount', 0) > 50
        if condition1 and condition2 and condition3 and condition4 and condition5:
            filtered_list.append(record)
    return filtered_list
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 15, 'status': 'active', 'date': '2023-05-10', 'amount': 100},
        {'id': 2, 'value': 5, 'status': 'active', 'date': '2023-05-11', 'amount': 200},
        {'id': 3, 'value': 12, 'status': 'inactive', 'date': '2023-06-15', 'amount': 300},
        {'id': 4, 'value': 20, 'status': 'active', 'date': '2024-01-01', 'amount': 40},
        {'id': 5, 'value': 11, 'status': 'active', 'date': '2022-12-31', 'amount': 60},
        {'id': 6, 'value': 10, 'status': 'active', 'date': '2023-01-01', 'amount': 55},
    ]
    result = process_records(sample_data)
    print(result)