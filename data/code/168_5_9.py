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
        {'id': 1, 'category': 'fruit', 'name': 'apple'},
        {'id': 2, 'category': 'vegetable', 'name': 'carrot'},
        {'id': 3, 'category': 'fruit', 'name': 'banana'},
        {'id': 4, 'category': 'meat', 'name': 'chicken'}
    ]
    grouped_records = group_by_field(sample_records, 'category')
    print(grouped_records)