from collections import defaultdict

def group_by_key(data, key):
    grouped = defaultdict(list)
    for item in data:
        grouped[item[key]].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'id': 101, 'type': 'car', 'year': 2020},
        {'id': 102, 'type': 'bike', 'year': 2018},
        {'id': 103, 'type': 'car', 'year': 2022},
        {'id': 104, 'type': 'motorcycle', 'year': 2019}
    ]
    grouped_data = group_by_key(sample_data, 'type')
    print(grouped_data)