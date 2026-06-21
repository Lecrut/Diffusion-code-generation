import functools
import operator

def get_nested_value(data, path):
    if not path:
        return data
    if not isinstance(data, (dict, list)):
        return None
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            if isinstance(current, list):
                index = int(key)
                current = current[index]
            elif isinstance(current, dict):
                current = current[key]
            else:
                return None
        return current
    except (KeyError, IndexError, ValueError, TypeError):
        return None

if __name__ == '__main__':
    sample_data = {
        'user': {
            'profile': {
                'contact': {
                    'email': 'example@test.com',
                    'phone': '123-456-7890'
                },
                'settings': {
                    'theme': 'dark',
                    'notifications': True
                }
            }
        },
        'items': [
            {'id': 1, 'name': 'alpha'},
            {'id': 2, 'name': 'beta'}
        ]
    }
    
    path1 = 'user.profile.contact.email'
    path2 = 'user.profile.settings.theme'
    path3 = 'items.1.name'
    path4 = 'user.profile.invalid.key'
    
    result1 = get_nested_value(sample_data, path1)
    result2 = get_nested_value(sample_data, path2)
    result3 = get_nested_value(sample_data, path3)
    result4 = get_nested_value(sample_data, path4)
    
    print(result1)
    print(result2)
    print(result3)
    print(result4)