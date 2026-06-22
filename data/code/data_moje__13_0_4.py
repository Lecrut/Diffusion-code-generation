def get_nested_value(data, path, default=None):
    current = data
    for key in path:
        if not isinstance(current, dict):
            return default
        if key not in current:
            return default
        current = current[key]
    return current

if __name__ == '__main__':
    sample_data = {
        'user': {
            'profile': {
                'name': 'Alice',
                'settings': {
                    'theme': 'dark',
                    'notifications': True
                }
            }
        }
    }
    path_found = ['user', 'profile', 'settings', 'theme']
    path_missing = ['user', 'profile', 'settings', 'language']
    path_invalid = ['user', 'profile', 'invalid_key']
    
    result_found = get_nested_value(sample_data, path_found, 'Not Found')
    result_missing = get_nested_value(sample_data, path_missing, 'Not Found')
    result_invalid = get_nested_value(sample_data, path_invalid, 'Not Found')
    
    print(result_found)
    print(result_missing)
    print(result_invalid)