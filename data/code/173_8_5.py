import collections
def group_by_attribute(data, attribute):
    groups = collections.defaultdict(list)
    for item in data:
        key = item[attribute]
        groups[key].append(item)
    return dict(groups)
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'city': 'New York', 'age': 30},
        {'name': 'Bob', 'city': 'Los Angeles', 'age': 25},
        {'name': 'Charlie', 'city': 'New York', 'age': 35},
        {'name': 'David', 'city': 'Chicago', 'age': 28},
        {'name': 'Eve', 'city': 'Los Angeles', 'age': 22},
        {'name': 'Frank', 'city': 'New York', 'age': 30}
    ]
    attribute_to_group_by = 'city'
    grouped_result = group_by_attribute(sample_data, attribute_to_group_by)
    print(grouped_result)