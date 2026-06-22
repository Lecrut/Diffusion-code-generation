def filter_records(records):
    def check_value(record):
        return record.get('value', 0) > 10

    def check_status(record):
        return record.get('status', '') == 'active'

    def check_date(record):
        date_str = record.get('date', '')
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
        except (ValueError, TypeError):
            return False

    def check_priority(record):
        return record.get('priority', 0) >= 5

    def check_category(record):
        return record.get('category', '') in ['A', 'B', 'C']

    filtered = []
    for record in records:
        if (check_value(record) and
            check_status(record) and
            check_date(record) and
            check_priority(record) and
            check_category(record)):
            filtered.append(record)
    return filtered

if __name__ == '__main__':
    sample_data = [
        {'value': 15, 'status': 'active', 'date': '2023-01-15', 'priority': 8, 'category': 'A'},
        {'value': 5, 'status': 'active', 'date': '2023-02-20', 'priority': 6, 'category': 'B'},
        {'value': 20, 'status': 'inactive', 'date': '2023-03-10', 'priority': 9, 'category': 'C'},
        {'value': 12, 'status': 'active', 'date': '2023-13-01', 'priority': 7, 'category': 'A'},
        {'value': 18, 'status': 'active', 'date': '2023-04-05', 'priority': 4, 'category': 'D'},
        {'value': 25, 'status': 'active', 'date': '2023-05-12', 'priority': 10, 'category': 'B'},
    ]
    result = filter_records(sample_data)
    print(result)