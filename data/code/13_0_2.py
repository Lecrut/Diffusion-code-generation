def get_nested_value(data, path, default=None):
    keys = path if isinstance(path, list) else path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

if __name__ == '__main__':
    sample_data = {
        'user': {
            'name': 'Alice',
            'address': {
                'city': 'Wonderland',
                'coordinates': {
                    'lat': 51.5074,
                    'lon': -0.1278
                }
            }
        },
        'settings': {
            'theme': 'dark',
            'notifications': {
                'email': True,
                'sms': False
            }
        }
    }

    result1 = get_nested_value(sample_data, ['user', 'address', 'city'], 'Unknown')
    print(result1)

    result2 = get_nested_value(sample_data, ['user', 'address', 'country'], 'Unknown')
    print(result2)

    result3 = get_nested_value(sample_data, ['settings', 'theme'], 'light')
    print(result3)

    result4 = get_nested_value(sample_data, ['nonexistent', 'path'], 'Default')
    print(result4)

    result5 = get_nested_value(sample_data, ['user', 'address', 'coordinates', 'lat'], 0.0)
    print(result5)

    empty_dict = {}
    result6 = get_nested_value(empty_dict, ['key'], 'Fallback')
    print(result6)

    nested_with_none = {'a': {'b': None}}
    result7 = get_nested_value(nested_with_none, ['a', 'b', 'c'], 'Not Found')
    print(result7)