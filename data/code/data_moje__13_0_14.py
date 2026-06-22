def get_nested_value(data, path, default=None):
    current = data
    for key in path:
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
            'y': 'hello'
        }
    }

    print(get_nested_value(sample_dict, ['a', 'b', 'c']))
    print(get_nested_value(sample_dict, ['a', 'b', 'missing'], 'default_val'))
    print(get_nested_value(sample_dict, ['x', 'y']))
    print(get_nested_value(sample_dict, ['nonexistent', 'path'], 0))