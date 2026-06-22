def filter_records(records):
    def is_value_gt_10(record):
        return record.get('value', 0) > 10

    def is_status_active(record):
        return record.get('status', '') == 'active'

    def is_date_valid(record):
        date_str = record.get('date', '')
        if not isinstance(date_str, str) or len(date_str) != 10:
            return False
        try:
            parts = date_str.split('-')
            if len(parts) != 3:
                return False
            year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
            if year < 1 or month < 1 or month > 12 or day < 1:
                return False
            if month in [4, 6, 9, 11] and day > 30:
                return False
            if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
                return False
            if month == 2:
                is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
                max_day = 29 if is_leap else 28
                if day > max_day:
                    return False
            return True
        except ValueError:
            return False

    def is_priority_high(record):
        return record.get('priority', 0) >= 5

    def is_category_valid(record):
        return record.get('category', '') in ['A', 'B', 'C']

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
        {'value': 15, 'status': 'active', 'date': '2023-02-28', 'priority': 5, 'category': 'A'},
        {'value': 5, 'status': 'active', 'date': '2023-02-28', 'priority': 5, 'category': 'A'},
        {'value': 15, 'status': 'inactive', 'date': '2023-02-28', 'priority': 5, 'category': 'A'},
        {'value': 15, 'status': 'active', 'date': '2023-02-29', 'priority': 5, 'category': 'A'},
        {'value': 15, 'status': 'active', 'date': '2023-02-28', 'priority': 4, 'category': 'A'},
        {'value': 15, 'status': 'active', 'date': '2023-02-28', 'priority': 5, 'category': 'D'},
        {'value': 20, 'status': 'active', 'date': '2023-02-28', 'priority': 6, 'category': 'B'},
    ]
    result = filter_records(sample_data)
    print(result)