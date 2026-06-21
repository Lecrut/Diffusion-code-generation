def get_nested_value(data, keys, default=None):
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

if __name__ == '__main__':
    sample_data = {
        'a': {
            'b': {
                'c': 42
            }
        },
        'x': {
            'y': [1, 2, 3]
        }
    }

    result1 = get_nested_value(sample_data, ['a', 'b', 'c'])
    print(result1)

    result2 = get_nested_value(sample_data, ['a', 'b', 'z'])
    print(result2)

    result3 = get_nested_value(sample_data, ['missing', 'key'])
    print(result3)

    result4 = get_nested_value(sample_data, ['x', 'y'])
    print(result4)

    result5 = get_nested_value(sample_data, ['a', 'b', 'c'], default='MISSING')
    print(result5)

    result6 = get_nested_value(sample_data, ['a', 'nonexistent'], default='DEFAULT_VALUE')
    print(result6)