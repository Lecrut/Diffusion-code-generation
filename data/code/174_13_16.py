from collections import defaultdict

def group_by_key(data, key):
    grouped_data = defaultdict(list)
    for item in data:
        grouped_data[item[key]].append(item)
    return dict(grouped_data)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'category': 'fruit', 'name': 'apple'},
        {'id': 2, 'category': 'vegetable', 'name': 'carrot'},
        {'id': 3, 'category': 'fruit', 'name': 'banana'},
        {'id': 4, 'category': 'grain', 'name': 'rice'}
    ]
    grouped = group_by_key(sample_data, 'category')
    print(grouped)