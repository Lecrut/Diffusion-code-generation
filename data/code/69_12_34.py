def retrieve_nested_value(data, keys):
    try:
        for key in keys:
            data = data[key]
        return data
    except KeyError:
        raise ValueError("Key not found in the nested dictionary")

if __name__ == '__main__':
    sample_data = {
        'level1': {
            'level2': {
                'level3': 'value'
            }
        }
    }
    keys_to_retrieve = ['level1', 'level2', 'level3']
    result = retrieve_nested_value(sample_data, keys_to_retrieve)
    print(result)