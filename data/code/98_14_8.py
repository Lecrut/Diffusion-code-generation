def process_records(data):
    filtered_list = []
    for record in data:
        condition1 = record.get('value', 0) > 10
        condition2 = record.get('status') == 'active'
        condition3 = '2023-01-01' <= record.get('date', '1900-01-01') <= '2024-12-31'
        condition4 = isinstance(record.get('data_point'), (int, float))
        condition5 = record.get('id') is not None
        if condition1 and condition2 and condition3 and condition4 and condition5:
            filtered_list.append(record)
    return filtered_list
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 15, 'status': 'active', 'date': '2023-05-10', 'data_point': 50},
        {'id': 2, 'value': 5, 'status': 'active', 'date': '2023-05-11', 'data_point': 100},
        {'id': 3, 'value': 20, 'status': 'inactive', 'date': '2023-05-12', 'data_point': 200},
        {'id': 4, 'value': 12, 'status': 'active', 'date': '2022-12-31', 'data_point': 'error'},
        {'id': 5, 'value': 11, 'status': 'active', 'date': '2024-01-01', 'data_point': 75},
        {'id': 6, 'value': 30, 'status': 'active', 'date': '2025-01-01', 'data_point': 10},
    ]
    result = process_records(sample_data)
    print(result)