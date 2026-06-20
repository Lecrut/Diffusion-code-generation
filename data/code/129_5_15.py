def group_and_sort(data, group_key, sort_key):
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("All items in the list must be dictionaries.")
    
    grouped_data = {}
    for item in data:
        key = item.get(group_key)
        if key is None:
            raise KeyError(f"Key '{group_key}' not found in one of the dictionaries.")
        
        if key not in grouped_data:
            grouped_data[key] = []
        grouped_data[key].append(item)
    
    sorted_data = {k: sorted(v, key=lambda x: x.get(sort_key), reverse=True) for k, v in grouped_data.items()}
    return sorted_data

if __name__ == '__main__':
    employee_data = [
        {'name': 'Alice', 'category': 'HR', 'value': 60000},
        {'name': 'Bob', 'category': 'Engineering', 'value': 95000},
        {'name': 'Charlie', 'category': 'HR', 'value': 75000}
    ]
    
    result = group_and_sort(employee_data, 'category', 'value')
    print(result)