def group_records(records, key_field):
    groups = {}
    for record in records:
        key_value = record[key_field]
        if key_value not in groups:
            groups[key_value] = []
        groups[key_value].append(record)
    return groups

if __name__ == '__main__':
    sample_records = [
        {'id': 1, 'type': 'X', 'data': 10},
        {'id': 2, 'type': 'Y', 'data': 20},
        {'id': 3, 'type': 'X', 'data': 30},
        {'id': 4, 'type': 'Z', 'data': 40},
        {'id': 5, 'type': 'Y', 'data': 50}
    ]
    grouped_records = group_records(sample_records, 'type')
    print(grouped_records)