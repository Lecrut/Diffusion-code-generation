def group_by_field(records, field):
    groups = {}
    for record in records:
        key = record[field]
        if key not in groups:
            groups[key] = []
        groups[key].append(record)
    return groups

if __name__ == '__main__':
    sample_records = [
        {'id': 1, 'category': 'A', 'value': 10},
        {'id': 2, 'category': 'B', 'value': 20},
        {'id': 3, 'category': 'A', 'value': 30},
        {'id': 4, 'category': 'C', 'value': 40},
        {'id': 5, 'category': 'B', 'value': 50}
    ]
    grouped_records = group_by_field(sample_records, 'category')
    print(grouped_records)