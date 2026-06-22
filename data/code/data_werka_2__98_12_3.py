def filter_records(records):
    def is_value_gt_10(record):
        return record.get('value', 0) > 10

    def is_status_active(record):
        return record.get('status') == 'active'

    def is_date_valid(record):
        date_str = record.get('date')
        if not isinstance(date_str, str):
            return False
        try:
            parts = date_str.split('-')
            if len(parts) != 3:
                return False
            year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
            if month < 1 or month > 12:
                return False
            if day < 1 or day > 31:
                return False
            return True
        except ValueError:
            return False

    def is_priority_high(record):
        priority = record.get('priority')
        return isinstance(priority, int) and priority >= 5

    def is_category_valid(record):
        category = record.get('category')
        valid_categories = ['A', 'B', 'C', 'D']
        return category in valid_categories

    filtered = []
    for record in records:
        if (is_value_gt_10(record) and
            is_status_active(record) and
            is_date_valid(record) and
            is_priority_high(record) and
            is_category_valid(record)):
            filtered.append(record)
    return filtered

if __name__ == '__main__':
    sample_data = [
        {'value': 15, 'status': 'active', 'date': '2023-10-01', 'priority': 5, 'category': 'A'},
        {'value': 5, 'status': 'active', 'date': '2023-10-02', 'priority': 6, 'category': 'B'},
        {'value': 20, 'status': 'inactive', 'date': '2023-10-03', 'priority': 7, 'category': 'C'},
        {'value': 12, 'status': 'active', 'date': 'invalid-date', 'priority': 8, 'category': 'D'},
        {'value': 18, 'status': 'active', 'date': '2023-11-15', 'priority': 4, 'category': 'A'},
        {'value': 25, 'status': 'active', 'date': '2023-12-25', 'priority': 9, 'category': 'E'},
        {'value': 30, 'status': 'active', 'date': '2024-01-01', 'priority': 10, 'category': 'B'},
    ]

    result = filter_records(sample_data)
    print(result)