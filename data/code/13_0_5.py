def get_nested_value(data, keys, default=None):
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

if __name__ == '__main__':
    sample_dict = {
        'level1': {
            'level2': {
                'level3': 'deep_value'
            }
        }
    }
    
    result1 = get_nested_value(sample_dict, ['level1', 'level2', 'level3'])
    print(result1)
    
    result2 = get_nested_value(sample_dict, ['level1', 'nonexistent'])
    print(result2)
    
    result3 = get_nested_value(sample_dict, ['level1', 'level2', 'level3'], 'default_value')
    print(result3)
    
    result4 = get_nested_value({}, ['key'], 'empty_dict_default')
    print(result4)