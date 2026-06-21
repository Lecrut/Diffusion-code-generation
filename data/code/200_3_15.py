def extract_keys(data_list, keys):
    if not all(isinstance(item, dict) for item in data_list):
        raise ValueError("All items in the list must be dictionaries.")
    if not all(isinstance(key, str) for key in keys):
        raise ValueError("All keys must be strings.")

    return [dict((k, item[k]) for k in keys if k in item) for item in data_list]

if __name__ == '__main__':
    sample_data = [
        {'name': 'Apple', 'value': 10, 'color': 'red'},
        {'name': 'Banana', 'value': 20, 'color': 'yellow'},
        {'name': 'Cherry', 'value': 30, 'color': 'red'}
    ]
    keys_to_extract = ['name', 'value']
    filtered_data = extract_keys(sample_data, keys_to_extract)
    print(filtered_data)