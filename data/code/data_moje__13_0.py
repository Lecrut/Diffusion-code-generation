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
            'version': '1.0'
        }
    }
    path_1 = ['user', 'profile', 'name']
    path_2 = ['user', 'profile', 'email']
    path_3 = ['user', 'settings', 'theme']
    path_4 = ['config', 'version', 'minor']
    
    result_1 = get_nested_value(sample_data, path_1, 'Unknown')
    result_2 = get_nested_value(sample_data, path_2, 'Unknown')
    result_3 = get_nested_value(sample_data, path_3, 'Unknown')
    result_4 = get_nested_value(sample_data, path_4, 'Unknown')
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)