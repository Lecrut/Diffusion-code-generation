def get_nested_value(data, path):
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict):
            if key not in current:
                raise KeyError(f"Key '{key}' not found in dictionary")
            current = current[key]
        elif isinstance(current, list):
            try:
                index = int(key)
            except ValueError:
                raise TypeError(f"Cannot index list with non-integer key '{key}'")
            if index < 0 or index >= len(current):
                raise IndexError(f"Index {index} out of range for list of length {len(current)}")
            current = current[index]
        else:
            raise TypeError(f"Cannot access child of non-container type '{type(current).__name__}'")
    return current

if __name__ == '__main__':
    sample_data = {
        'user': {
            'profile': {
                'name': 'Alice',
                'address': {
                    'city': 'Wonderland',
                    'zip': '12345'
                }
            },
            'friends': ['Bob', 'Charlie']
        },
        'metadata': {
            'version': 1
        }
    }
    
    path1 = 'user.profile.name'
    path2 = 'user.friends.0'
    path3 = 'user.profile.address.city'
    
    print(get_nested_value(sample_data, path1))
    print(get_nested_value(sample_data, path2))
    print(get_nested_value(sample_data, path3))