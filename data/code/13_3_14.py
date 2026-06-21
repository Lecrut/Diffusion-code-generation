def get_nested_value(data, path):
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list):
            try:
                index = int(key)
                current = current[index]
            except (ValueError, IndexError):
                raise KeyError(f"Invalid list index: {key}")
        else:
            raise KeyError(f"Key not found: {key}")
    return current

if __name__ == '__main__':
    sample_data = {
        'level1': {
            'level2': {
                'level3': 'deep_value'
            }
        },
        'list_key': [
            {'item': 'first'},
            {'item': 'second'}
        ]
    }
    result1 = get_nested_value(sample_data, 'level1.level2.level3')
    print(result1)
    result2 = get_nested_value(sample_data, 'list_key.1.item')
    print(result2)