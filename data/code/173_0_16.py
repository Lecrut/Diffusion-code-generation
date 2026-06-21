from collections import defaultdict

def group_by_key(data, key):
    grouped = defaultdict(list)
    for item in data:
        grouped[item[key]].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'category': 'fruit', 'name': 'apple'},
        {'category': 'vegetable', 'name': 'carrot'},
        {'category': 'fruit', 'name': 'banana'},
        {'category': 'meat', 'name': 'chicken'}
    ]
    grouped_data = group_by_key(sample_data, 'category')
    print(grouped_data)