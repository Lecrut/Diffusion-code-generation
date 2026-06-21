from collections import defaultdict

def validate_input(data_list, key):
    if not all(isinstance(item, dict) for item in data_list):
        raise ValueError("All items in the list must be dictionaries.")
    if not any(key in item for item in data_list):
        raise KeyError(f"Key '{key}' not found in any dictionary.")

def group_data(data_list, key):
    validate_input(data_list, key)
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
    result = group_data(sample_data, grouping_key)
    print(result)