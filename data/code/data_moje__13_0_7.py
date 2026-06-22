def get_nested_value(nested_dict, key_path, default=None):
    current = nested_dict
    for key in key_path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

if __name__ == '__main__':
    sample_dict = {
        'a': {
            'b': {
                'c': 42,
                'd': [1, 2, 3]
            },
            'e': 'hello'
        },
        'f': None
    }
    result1 = get_nested_value(sample_dict, ['a', 'b', 'c'])
    print(result1)
    result2 = get_nested_value(sample_dict, ['a', 'b', 'x'])
    print(result2)
    result3 = get_nested_value(sample_dict, ['a', 'e'])
    print(result3)
    result4 = get_nested_value(sample_dict, ['nonexistent', 'key'], 'default_val')
    print(result4)
    result5 = get_nested_value(sample_dict, ['a', 'b', 'd'])
    print(result5)
    result6 = get_nested_value(sample_dict, [])
    print(result6)