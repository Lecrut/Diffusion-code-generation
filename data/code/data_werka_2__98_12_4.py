def filter_records(records):
    def is_valid_date(date_str):
        try:
            parts = date_str.split('-')
            if len(parts) != 3:
                return False
            year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
            if year < 1900 or year > 2100:
                return False
            if month < 1 or month > 12:
                return False
            if day < 1 or day > 31:
                return False
            return True
        except (ValueError, AttributeError):
            return False

    filtered = []
    for record in records:
        value = record.get('value', 0)
        status = record.get('status', '')
        date = record.get('date', '')
        category = record.get('category', '')
        priority = record.get('priority', 0)

        cond1 = value > 10
        cond2 = status == 'active'
        cond3 = is_valid_date(date)
        cond4 = category in ['A', 'B', 'C']
        cond5 = priority >= 1

        if cond1 and cond2 and cond3 and cond4 and cond5:
            filtered.append(record)

    return filtered

if __name__ == '__main__':
    sample_data = [
        {'value': 15, 'status': 'active', 'date': '2023-01-15', 'category': 'A', 'priority': 2},
        {'value': 5, 'status': 'active', 'date': '2023-02-20', 'category': 'B', 'priority': 1},
        {'value': 20, 'status': 'inactive', 'date': '2023-03-10', 'category': 'C', 'priority': 3},
        {'value': 25, 'status': 'active', 'date': '2023-13-01', 'category': 'D', 'priority': 1},
        {'value': 30, 'status': 'active', 'date': '2023-04-05', 'category': 'A', 'priority': 0},
        {'value': 50, 'status': 'active', 'date': '2023-05-10', 'category': 'B', 'priority': 5},
    ]

    result = filter_records(sample_data)
    print(result)