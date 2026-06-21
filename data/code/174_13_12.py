from collections import defaultdict

def group_by_key(data_list, key):
    grouped_dict = defaultdict(list)
    for item in data_list:
        grouped_dict[item[key]].append(item)
    return dict(grouped_dict)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'type': 'fruit', 'name': 'apple'},
        {'id': 2, 'type': 'vegetable', 'name': 'carrot'},
        {'id': 3, 'type': 'fruit', 'name': 'banana'},
        {'id': 4, 'type': 'fruit', 'name': 'cherry'}
    ]
    grouped_data = group_by_key(sample_data, 'type')
    print(grouped_data)