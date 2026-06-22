from datetime import datetime

def filter_records(records):
    valid_categories = {'A', 'B', 'C'}
    filtered = []
    for record in records:
        value = record.get('value')
        status = record.get('status')
        date_str = record.get('date')
        category = record.get('category')
        priority = record.get('priority')
        if not isinstance(value, (int, float)) or value <= 10:
            continue
        if status != 'active':
            continue
        if date_str is None:
            continue
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except (ValueError, TypeError):
            continue
        if category not in valid_categories:
            continue
        if not isinstance(priority, (int, float)) or priority < 1:
            continue
        filtered.append(record)
    return filtered
if __name__ == '__main__':
    sample_records = [{'value': 15, 'status': 'active', 'date': '2023-01-15', 'category': 'A', 'priority': 2}, {'value': 5, 'status': 'active', 'date': '2023-02-20', 'category': 'B', 'priority': 3}, {'value': 20, 'status': 'inactive', 'date': '2023-03-10', 'category': 'C', 'priority': 1}, {'value': 25, 'status': 'active', 'date': None, 'category': 'A', 'priority': 4}, {'value': 30, 'status': 'active', 'date': '2023-04-05', 'category': 'D', 'priority': 5}, {'value': 12, 'status': 'active', 'date': '2023-05-12', 'category': 'B', 'priority': 0}, {'value': 50, 'status': 'active', 'date': '2023-06-18', 'category': 'C', 'priority': 1}]
    result = filter_records(sample_records)
    print(result)