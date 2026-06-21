from collections import defaultdict
DEFAULT_CATEGORY = 'Uncategorized'

def group_dictionaries_by_key(dict_list, key):
    grouped_dict = defaultdict(list)
    for item in dict_list:
        category = item.get(key, DEFAULT_CATEGORY)
        grouped_dict[category].append(item)
    return dict(grouped_dict)
if __name__ == '__main__':
    sample_dicts = [{'type': 'fruit', 'name': 'apple'}, {'type': 'vegetable', 'name': 'carrot'}, {'type': 'fruit', 'name': 'banana'}, {'type': 'meat', 'name': 'steak'}]
    grouped_by_type = group_dictionaries_by_key(sample_dicts, 'type')
    print(grouped_by_type)