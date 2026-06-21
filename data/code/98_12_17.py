from datetime import datetime

def filter_records(records):
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
            datetime.strptime(str(date_str), '%Y-%m-%d')
        except (ValueError, TypeError):
            continue
        if not category or not str(category).strip():
            continue
        if not isinstance(priority, (int, float)) or priority <= 0:
            continue
        filtered.append(record)
    return filtered
if __name__ == '__main__':
    sample_records = [{'value': 15, 'status': 'active', 'date': '2023-01-15', 'category': 'electronics', 'priority': 2}, {'value': 5, 'status': 'active', 'date': '2023-01-16', 'category': 'books', 'priority': 1}, {'value': 20, 'status': 'inactive', 'date': '2023-01-17', 'category': 'clothing', 'priority': 3}, {'value': 25, 'status': 'active', 'date': None, 'category': 'food', 'priority': 1}, {'value': 30, 'status': 'active', 'date': '2023-01-19', 'category': '', 'priority': 2}, {'value': 12, 'status': 'active', 'date': '2023-01-20', 'category': 'sports', 'priority': 0}, {'value': 50, 'status': 'active', 'date': '2023-01-21', 'category': 'furniture', 'priority': 5}, {'value': 100, 'status': 'active', 'date': '2023-01-22', 'category': 'toys', 'priority': 3}]
    result = filter_records(sample_records)
    print(result)