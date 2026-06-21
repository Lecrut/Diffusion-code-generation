def group_records(records, key_field):
    groups = {}
    for record in records:
        key_value = record[key_field]
        if key_value not in groups:
            groups[key_value] = []
        groups[key_value].append(record)
    return groups

def validate_records(records, key_field):
    if not isinstance(records, list):
        raise ValueError("Records must be a list")
    if not records:
        raise ValueError("Records list cannot be empty")
    if not all(isinstance(record, dict) for record in records):
        raise ValueError("All records must be dictionaries")

if __name__ == '__main__':
    sample_records = [
        {'id': 1, 'category': 'A', 'value': 10},
        {'id': 2, 'category': 'B', 'value': 20},
        {'id': 3, 'category': 'A', 'value': 30},
        {'id': 4, 'category': 'C', 'value': 40},
        {'id': 5, 'category': 'B', 'value': 50}
    ]
    validate_records(sample_records, 'category')
    grouped_records = group_records(sample_records, 'category')
    print(grouped_records)