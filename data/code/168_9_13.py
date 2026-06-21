def group_items(data):
    def is_valid_key(key):
        if not isinstance(key, (str, int)):
            raise ValueError("Key must be a string or an integer")
        return True

    grouped = {}
    for item in data:
        if not isinstance(item, dict):
            continue
        
        keys = tuple(item.get(k) for k in ('key1', 'key2'))
        if any(not is_valid_key(key) for key in keys):
            continue
        
        current_group = grouped
        for key in keys[:-1]:
            if key not in current_group:
                current_group[key] = {}
            current_group = current_group[key]
        
        last_key = keys[-1]
        if last_key not in current_group:
            current_group[last_key] = []
        current_group[last_key].append(item)
    
    return grouped

if __name__ == '__main__':
    data = [
        {'key1': 'a', 'key2': 1, 'value': 10},
        {'key1': 'b', 'key2': 2, 'value': 20},
        {'key1': 'a', 'key2': 1, 'value': 30},
        {'key1': 'c', 'key2': 3, 'value': 40}
    ]
    print(group_items(data))