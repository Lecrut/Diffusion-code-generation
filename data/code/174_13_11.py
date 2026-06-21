from collections import defaultdict

GROUP_KEY = 'category'

def group_dictionaries(data):
    grouped_data = defaultdict(list)
    for item in data:
        key = item.get(GROUP_KEY, None)
        if key is not None:
            grouped_data[key].append(item)
    return dict(grouped_data)

if __name__ == '__main__':
    sample_data = [
        {'category': 'fruit', 'name': 'apple'},
        {'category': 'vegetable', 'name': 'carrot'},
        {'category': 'fruit', 'name': 'banana'},
        {'category': 'grain', 'name': 'rice'}
    ]
    grouped_result = group_dictionaries(sample_data)
    print(grouped_result)