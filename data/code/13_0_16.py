def get_nested_value(data, keys, default=None):
    current = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current

if __name__ == '__main__':
    sample_data = {
        'user': {
            'profile': {
                'name': 'Alice',
                'settings': {
                    'theme': 'dark'
                }
            }
        }
    }
    result1 = get_nested_value(sample_data, ['user', 'profile', 'name'], 'Unknown')
    result2 = get_nested_value(sample_data, ['user', 'profile', 'settings', 'language'], 'English')
    result3 = get_nested_value(sample_data, ['user', 'email'], 'N/A')
    print(result1)
    print(result2)
    print(result3)