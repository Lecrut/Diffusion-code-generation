from collections import defaultdict

def group_by_key(data, key):
    grouped = defaultdict(list)
    for item in data:
        grouped[item[key]].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'type': 'car', 'make': 'Toyota'},
        {'type': 'bike', 'make': 'Harley-Davidson'},
        {'type': 'car', 'make': 'Ford'},
        {'type': 'bike', 'make': 'Yamaha'}
    ]
    grouped_by_type = group_by_key(sample_data, 'type')
    print(grouped_by_type)