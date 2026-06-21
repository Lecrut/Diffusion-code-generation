def filter_keys(data_list, keys):
    if not all(isinstance(item, dict) for item in data_list):
        raise ValueError("All items in data_list must be dictionaries")
    if not all(isinstance(key, str) for key in keys):
        raise ValueError("All keys in keys list must be strings")
    
    return [{key: item[key] for key in keys if key in item} for item in data_list]

if __name__ == '__main__':
    sample_data = [
        {'name': 'Apple', 'value': 10, 'color': 'Red'},
        {'name': 'Banana', 'value': 20, 'color': 'Yellow'},
        {'name': 'Cherry', 'value': 30, 'color': 'Red'}
    ]
    keys = ['name', 'value']
    filtered_data = filter_keys(sample_data, keys)
    print(filtered_data)