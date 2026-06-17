def get_nested_value(data: dict, path: list) -> any:
    current = data
    for key in path:
        if isinstance(current, dict):
            value = current.get(key)
            if value is not None:
                return value
            else:
                return default
        elif isinstance(value, (list, tuple)):
            try:
                index = int(path[-1])
                item = value[index]
                for k in path[1:-1]:
                    current_item = get_nested_value(item, [k])
                return current_item
            except IndexError:
                return default
        else:
            return None
def safe_get(data: dict, *keys) -> any:
    if not keys:
        return data.get('value')
    path = list(keys)
    result = get_nested_value(data, path)
    return result
if __name__ == '__main__':
    sample_data = {
        'level1': {
            'level2': {
                'optional_field': None,
                'required_field': 42
            }
        },
        'another_level': {
            'deeply_nested': {
                'data': {'target_key': 'found_value'}
            }
        }
    }
    result1 = safe_get(sample_data, 'level1', 'optional_field')
    print(result1)                                                                                                                                                                                                                                     
    result2 = safe_get(sample_data, 'level1', 'required_field')
    print(result2)              
    result3 = safe_get(sample_data, 'another_level', 'deeply_nested', 'data', 'target_key')
    print(result3)                       
    default_val = None if not hasattr(safe_get, '_default_arg') else getattr(safe_get, '_default_arg')