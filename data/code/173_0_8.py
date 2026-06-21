from collections import defaultdict

def group_records(records, key):
    grouped = defaultdict(list)
    for record in records:
        if key in record:
            category = record[key]
            grouped[category].append(record)
    return dict(grouped)

if __name__ == '__main__':
    sample_records = [
        {'id': 101, 'department': 'Engineering', 'employee': 'Alice'},
        {'id': 102, 'department': 'HR', 'employee': 'Bob'},
        {'id': 103, 'department': 'Engineering', 'employee': 'Charlie'},
        {'id': 104, 'department': 'Marketing', 'employee': 'David'},
        {'id': 105, 'department': 'HR', 'employee': 'Eve'}
    ]
    department_key = 'department'
    grouped_records = group_records(sample_records, department_key)
    print(grouped_records)