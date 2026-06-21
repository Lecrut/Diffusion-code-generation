from collections import defaultdict

def group_by_key(data, key):
    grouped = defaultdict(list)
    for item in data:
        grouped[item[key]].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'category': 'fruit', 'value': 10},
        {'id': 2, 'category': 'vegetable', 'value': 5},
        {'id': 3, 'category': 'fruit', 'value': 7},
        {'id': 4, 'category': 'meat', 'value': 20}
    ]
    print(group_by_key(sample_data, 'category'))