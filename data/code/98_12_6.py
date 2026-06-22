def filter_records(records):
    def is_value_greater_than_10(record):
        return record.get('value', 0) > 10

    def is_status_active(record):
        return record.get('status') == 'active'

    def is_date_valid(record):
        date_str = record.get('date', '')
        if not isinstance(date_str, str) or len(date_str) != 10:
            return False
        try:
            parts = date_str.split('-')
            year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
            if month < 1 or month > 12:
                return False
            if day < 1 or day > 31:
                return False
            return True
        except (ValueError, IndexError):
            return False

    def is_priority_high(record):
        return record.get('priority') in ('high', 'critical')

    def is_category_valid(record):
        return record.get('category') in ('A', 'B', 'C')

    filtered = []
    for record in records:
        if (is_value_greater_than_10(record) and
            is_status_active(record) and
            is_date_valid(record) and
            is_priority_high(record) and
            is_category_valid(record)):
            filtered.append(record)
    return filtered

if __name__ == '__main__':
    sample_data = [
        {'value': 15, 'status': 'active', 'date': '2023-01-15', 'priority': 'high', 'category': 'A'},
        {'value': 5, 'status': 'active', 'date': '2023-02-20', 'priority': 'high', 'category': 'B'},
        {'value': 20, 'status': 'inactive', 'date': '2023-03-10', 'priority': 'high', 'category': 'A'},
        {'value': 25, 'status': 'active', 'date': '2023-13-01', 'priority': 'high', 'category': 'A'},
        {'value': 30, 'status': 'active', 'date': '2023-04-05', 'priority': 'low', 'category': 'A'},
        {'value': 50, 'status': 'active', 'date': '2023-05-10', 'priority': 'high', 'category': 'D'},
        {'value': 12, 'status': 'active', 'date': '2023-06-15', 'priority': 'critical', 'category': 'C'},
    ]
    result = filter_records(sample_data)
    print(result)