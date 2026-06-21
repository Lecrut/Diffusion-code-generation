def filter_records(records):
    def validate_record(record):
        if not isinstance(record, dict):
            raise ValueError("Record must be a dictionary")
        if 'value' not in record or 'category' not in record:
            raise ValueError("Record must contain 'value' and 'category' keys")
        return record['value'], record['category']

    def check_condition(value, category):
        return (value > 100 and category == 'A') or (value == 0)

    if not isinstance(records, list):
        raise ValueError("Input must be a list of records")

    result = []
    for record in records:
        value, category = validate_record(record)
        if check_condition(value, category):
            result.append(record)
    return result

if __name__ == '__main__':
    sample_data = [
        {'value': 150, 'category': 'A'},
        {'value': 50, 'category': 'A'},
        {'value': 200, 'category': 'B'},
        {'value': 0, 'category': 'A'},
        {'value': 100, 'category': 'A'},
        {'value': 101, 'category': 'B'},
        {'value': 0, 'category': 'B'},
        {'value': 101, 'category': 'A'},
        {'value': 100, 'category': 'B'},
    ]
    print(filter_records(sample_data))