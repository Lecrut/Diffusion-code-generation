def get_nested_elements(data_dict, keys):
    if not isinstance(keys, list) or not all(isinstance(key, str) for key in keys):
        raise ValueError("Keys must be a list of strings")
    result = data_dict
    for key in keys:
        if key in result:
            result = result[key]
        else:
            return None
    return result

if __name__ == '__main__':
    sample_data = {
        'level1': {
            'level2': {
                'level3': {
                    'data': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                }
            }
        }
    }
    keys = ['level1', 'level2', 'level3', 'data']
    print(f"Extracted data: {get_nested_elements(sample_data, keys)}")