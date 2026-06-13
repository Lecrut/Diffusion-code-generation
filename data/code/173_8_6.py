import collections
def group_by_attribute(data, key_func):
    groups = collections.defaultdict(list)
    for item in data:
        key = key_func(item)
        groups[key].append(item)
    return dict(groups)
if __name__ == '__main__':
    large_list = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 30, 'city': 'New York'},
        {'name': 'David', 'age': 35, 'city': 'Chicago'},
        {'name': 'Eve', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Frank', 'age': 40, 'city': 'New York'},
    ]
    def get_city(obj):
        return obj['city']
    grouped_data = group_by_attribute(large_list, get_city)
    print(grouped_data)