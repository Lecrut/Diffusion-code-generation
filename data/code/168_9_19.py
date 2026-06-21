from collections import defaultdict

def group_items(data):
    grouped = defaultdict(dict)
    for item in data:
        key1 = item.get('key1', 'Other')
        key2 = item.get('key2', 'Other')
        if key1 not in grouped:
            grouped[key1] = {}
        if key2 not in grouped[key1]:
            grouped[key1][key2] = []
        grouped[key1][key2].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'key1': 'A', 'key2': 'X', 'value': 1},
        {'key1': 'B', 'key2': 'Y', 'value': 2},
        {'key1': 'A', 'key2': 'X', 'value': 3},
        {'key1': 'C', 'key2': 'Z', 'value': 4}
    ]
    print(group_items(sample_data))