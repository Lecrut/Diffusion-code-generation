def get_nested_value(data, path, default=None):
    current = data
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current

if __name__ == '__main__':
    sample_data = {
        'user': {
            'profile': {
                'name': 'Alice',
                'age': 30
            },
            'settings': {
                'theme': 'dark'
            }
        },
        'config': {
            'debug': True
        }
    }
    
    print(get_nested_value(sample_data, ['user', 'profile', 'name'], 'Unknown'))
    print(get_nested_value(sample_data, ['user', 'profile', 'email'], 'Not Found'))
    print(get_nested_value(sample_data, ['user', 'settings', 'theme'], 'Light'))
    print(get_nested_value(sample_data, ['user', 'profile', 'missing', 'deep'], 'Default'))
    print(get_nested_value(sample_data, ['config', 'debug'], 'False'))