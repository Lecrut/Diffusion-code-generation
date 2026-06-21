def get_nested_value(d, keys, default=None):
    current = d
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

if __name__ == '__main__':
    sample_dict = {
        'a': {
            'b': {
                'c': 42
            }
        },
        'x': {
            'y': None
        }
    }

    result1 = get_nested_value(sample_dict, ['a', 'b', 'c'])
    print(result1)

    result2 = get_nested_value(sample_dict, ['a', 'b', 'missing'], 'default_value')
    print(result2)

    result3 = get_nested_value(sample_dict, ['x', 'y'])
    print(result3)

    result4 = get_nested_value(sample_dict, ['nonexistent'], 0)
    print(result4)