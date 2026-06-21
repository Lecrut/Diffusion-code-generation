from collections import defaultdict

def group_entries(data_list, category_key):
    grouped_data = defaultdict(list)
    for entry in data_list:
        if category_key in entry:
            category = entry[category_key]
            grouped_data[category].append(entry)
    return dict(grouped_data)

if __name__ == '__main__':
    sample_data = [
        {'item': 'apple', 'section': 'fruit'},
        {'item': 'banana', 'section': 'fruit'},
        {'item': 'carrot', 'section': 'vegetable'},
        {'item': 'pear', 'section': 'fruit'}
    ]
    grouping_key = 'section'
    
    result = group_entries(sample_data, grouping_key)
    print(result)