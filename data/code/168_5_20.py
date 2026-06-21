def group_records(records, key_field):
    groups = {}
    for record in records:
        key_value = record.get(key_field)
        if key_value not in groups:
            groups[key_value] = []
        groups[key_value].append(record)
    return groups

if __name__ == '__main__':
    sample_records = [
        {'id': 1, 'category': 'A', 'value': 10},
        {'id': 2, 'category': 'B', 'value': 20},
        {'id': 3, 'category': 'A', 'value': 30},
        {'id': 4, 'category': 'C', 'value': 40},
        {'id': 5, 'category': 'B', 'value': 50}
    ]
    grouped_records = group_records(sample_records, 'category')
    print(grouped_records)