from collections import defaultdict

def group_and_sort(objects, group_attr, sort_attr):
    grouped = defaultdict(list)
    for obj in objects:
        grouped[obj[group_attr]].append(obj)
    
    for key, value_list in grouped.items():
        grouped[key] = sorted(value_list, key=lambda x: x[sort_attr], reverse=True)
    
    return dict(grouped)

if __name__ == '__main__':
    sample_objects = [
        {'category': 'A', 'value': 3},
        {'category': 'B', 'value': 1},
        {'category': 'A', 'value': 2},
        {'category': 'B', 'value': 4}
    ]
    
    result = group_and_sort(sample_objects, 'category', 'value')
    print(result)