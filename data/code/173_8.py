import collections
def group_by_attribute(data, key):
    groups = collections.defaultdict(list)
    for item in data:
        if key in item:
            attribute_value = item[key]
            groups[attribute_value].append(item)
    return dict(groups)
if __name__ == '__main__':
    large_list = [
        {'name': 'Alice', 'city': 'New York', 'age': 30},
        {'name': 'Bob', 'city': 'Los Angeles', 'age': 25},
        {'name': 'Charlie', 'city': 'New York', 'age': 35},
        {'name': 'David', 'city': 'Chicago', 'age': 30},
        {'name': 'Eve', 'city': 'Los Angeles', 'age': 28},
        {'name': 'Frank', 'city': 'New York', 'age': 40}
    ]
    attribute_to_group_by = 'city'
    grouped_data = group_by_attribute(large_list, attribute_to_group_by)
    print(grouped_data)