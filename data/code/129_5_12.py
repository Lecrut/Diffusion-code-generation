from collections import defaultdict

def group_and_sort(data, group_key, sort_key):
    grouped = defaultdict(list)
    for item in data:
        grouped[item[group_key]].append(item)
    
    sorted_groups = {key: sorted(group, key=lambda x: x[sort_key], reverse=True) for key, group in grouped.items()}
    return dict(sorted_groups)

if __name__ == '__main__':
    sample_data = [
        {'category': 'A', 'value': 3},
        {'category': 'B', 'value': 1},
        {'category': 'A', 'value': 2},
        {'category': 'C', 'value': 4},
        {'category': 'B', 'value': 5}
    ]
    
    result = group_and_sort(sample_data, 'category', 'value')
    print(result)