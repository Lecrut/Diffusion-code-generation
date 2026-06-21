from collections import defaultdict

def validate_data(data_list, key):
    if not isinstance(data_list, list):
        raise ValueError("data_list must be a list")
    for item in data_list:
        if not isinstance(item, dict):
            raise ValueError("each item in data_list must be a dictionary")
        if key not in item:
            raise KeyError(f"key '{key}' not found in all dictionaries")

def group_data(data_list, key):
    validate_data(data_list, key)
    grouped_data = defaultdict(list)
    for item in data_list:
        category = item[key]
        grouped_data[category].append(item)
    return dict(grouped_data)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'city': 'New York', 'age': 30},
        {'name': 'Bob', 'city': 'Los Angeles', 'age': 25},
        {'name': 'Charlie', 'city': 'New York', 'age': 35},
        {'name': 'David', 'city': 'Chicago', 'age': 28},
        {'name': 'Eve', 'city': 'Los Angeles', 'age': 22}
    ]
    grouping_key = 'city'
    grouped_data = group_data(sample_data, grouping_key)
    print(grouped_data)