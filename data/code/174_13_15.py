from collections import defaultdict

GROUP_KEY = 'category'

def group_by_key(data_list):
    grouped_data = defaultdict(list)
    for item in data_list:
        category = item.get(GROUP_KEY, 'default')
        grouped_data[category].append(item)
    return dict(grouped_data)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30, 'category': 'group1'},
        {'name': 'Bob', 'age': 25, 'category': 'group2'},
        {'name': 'Charlie', 'age': 35, 'category': 'group1'},
        {'name': 'David', 'age': 40, 'category': 'group3'}
    ]
    grouped = group_by_key(sample_data)
    print(grouped)