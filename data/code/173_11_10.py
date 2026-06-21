from collections import defaultdict

def group_by_key(data, key):
    grouped = defaultdict(list)
    for item in data:
        grouped[item[key]].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'user_id': 101, 'department': 'Engineering'},
        {'user_id': 102, 'department': 'HR'},
        {'user_id': 103, 'department': 'Engineering'},
        {'user_id': 104, 'department': 'Marketing'}
    ]
    
    grouped_data = group_by_key(sample_data, 'department')
    print(grouped_data)