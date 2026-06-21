def get_nested_value(data, path):
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict):
            if key not in current:
                raise KeyError(key)
            current = current[key]
        elif isinstance(current, list):
            if key.isdigit():
                index = int(key)
                if 0 <= index < len(current):
                    current = current[index]
                else:
                    raise IndexError(index)
            else:
                raise TypeError(f"Cannot access key '{key}' on list")
        else:
            raise AttributeError(f"Cannot access key '{key}' on {type(current).__name__}")
    return current

if __name__ == '__main__':
    sample_data = {
        'level1': {
            'level2': {
                'level3': {
                    'value': 42
                }
            }
        }
    }
    result = get_nested_value(sample_data, 'level1.level2.level3.value')
    print(result)