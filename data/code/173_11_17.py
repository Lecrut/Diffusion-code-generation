from collections import defaultdict

def group_by_key(data, key):
    grouped = defaultdict(list)
    for item in data:
        grouped[item[key]].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'type': 'A'},
        {'id': 2, 'type': 'B'},
        {'id': 3, 'type': 'A'},
        {'id': 4, 'type': 'C'}
    ]
    grouped_by_type = group_by_key(sample_data, 'type')
    print(grouped_by_type)