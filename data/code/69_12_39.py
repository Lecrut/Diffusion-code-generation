def validate_keys(keys):
    if not isinstance(keys, list) or not all(isinstance(key, (str, int)) for key in keys):
        raise ValueError('Keys must be a list of strings or integers')

def retrieve_nested_value(data, keys):
    validate_keys(keys)
    try:
        value = data
        for key in keys:
            value = value[key]
        return value
    except (KeyError, TypeError) as e:
        raise ValueError('Invalid keys or data structure') from e

if __name__ == '__main__':
    sample_data = {
        'level1': {
            'level2a': {
                'level3a': 99,
                'level3b': 'world'
            },
            'level2b': [10, 20, 30]
        },
        'level1b': False
    }
    
    keys_to_retrieve = ['level1', 'level2a', 'level3a']
    print(retrieve_nested_value(sample_data, keys_to_retrieve))
    
    keys_to_retrieve = ['level1', 'level2b', 1]
    print(retrieve_nested_value(sample_data, keys_to_retrieve))
    
    keys_to_retrieve = ['level1b']
    print(retrieve_nested_value(sample_data, keys_to_retrieve))