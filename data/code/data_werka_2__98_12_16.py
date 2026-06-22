def filter_records(records):
    def validate_value(record):
        val = record.get('value')
        if not isinstance(val, (int, float)):
            return False
        return val > 10

    def validate_status(record):
        status = record.get('status')
        return status == 'active'

    def validate_date(record):
        date_str = record.get('date')
        if not isinstance(date_str, str):
            return False
        try:
            parts = date_str.split('-')
            if len(parts) != 3:
                return False
            year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
            if not (1 <= month <= 12):
                return False
            if not (1 <= day <= 31):
                return False
            if not (1 <= year <= 9999):
                return False
            return True
        except (ValueError, TypeError):
            return False

    def validate_priority(record):
        priority = record.get('priority')
        if not isinstance(priority, int):
            return False
        return priority >= 1

    def validate_category(record):
        category = record.get('category')
        return isinstance(category, str) and len(category) > 0

    results = []
    for record in records:
        if validate_value(record) and validate_status(record) and validate_date(record) and validate_priority(record) and validate_category(record):
            results.append(record)
    return results

if __name__ == '__main__':
    sample_data = [
        {'value': 15, 'status': 'active', 'date': '2023-05-15', 'priority': 1, 'category': 'A'},
        {'value': 5, 'status': 'active', 'date': '2023-05-15', 'priority': 1, 'category': 'A'},
        {'value': 12, 'status': 'inactive', 'date': '2023-05-15', 'priority': 1, 'category': 'B'},
        {'value': 20, 'status': 'active', 'date': '2023-13-01', 'priority': 1, 'category': 'C'},
        {'value': 25, 'status': 'active', 'date': '2023-06-10', 'priority': 0, 'category': 'D'},
        {'value': 30, 'status': 'active', 'date': '2023-07-20', 'priority': 2, 'category': ''},
        {'value': 50, 'status': 'active', 'date': '2023-08-25', 'priority': 3, 'category': 'E'},
    ]
    filtered_data = filter_records(sample_data)
    print(filtered_data)