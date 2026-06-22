def filter_records(data):
    if not isinstance(data, list):
        raise ValueError("Input data must be a list")
    
    def validate_record(record):
        if not isinstance(record, dict):
            raise ValueError("Each record must be a dictionary")
        if 'value' not in record or 'category' not in record:
            raise ValueError("Each record must contain 'value' and 'category' keys")
        return record

    def check_condition(record):
        value = record['value']
        category = record['category']
        first_part = (value > 100) and (category == 'A')
        second_part = (value == 0)
        return first_part or second_part

    result = []
    for item in data:
        validated = validate_record(item)
        if check_condition(validated):
            result.append(validated)
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
        {'value': 101, 'category': 'A'}
    ]
    print(filter_records(sample_data))