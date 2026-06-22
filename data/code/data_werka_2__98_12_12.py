def filter_records(records):
    valid_records = []
    for record in records:
        value = record.get('value', 0)
        status = record.get('status', '')
        date_str = record.get('date', '')
        category = record.get('category', '')
        priority = record.get('priority', 0)
        
        cond1 = value > 10
        cond2 = status == 'active'
        cond3 = len(date_str) == 10 and date_str[4] == '-' and date_str[7] == '-'
        cond4 = category in ['A', 'B', 'C']
        cond5 = priority >= 5
        
        if cond1 and cond2 and cond3 and cond4 and cond5:
            valid_records.append(record)
    return valid_records

if __name__ == '__main__':
    sample_data = [
        {'value': 15, 'status': 'active', 'date': '2023-01-01', 'category': 'A', 'priority': 5},
        {'value': 5, 'status': 'active', 'date': '2023-01-02', 'category': 'A', 'priority': 5},
        {'value': 20, 'status': 'inactive', 'date': '2023-01-03', 'category': 'B', 'priority': 10},
        {'value': 25, 'status': 'active', 'date': '2023-01-04', 'category': 'D', 'priority': 8},
        {'value': 30, 'status': 'active', 'date': '2023-01-05', 'category': 'C', 'priority': 12},
        {'value': 50, 'status': 'active', 'date': 'bad-date', 'category': 'A', 'priority': 15},
    ]
    
    result = filter_records(sample_data)
    print(result)