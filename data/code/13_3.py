def resolve_nested_value(data, path):
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict):
            if key in current:
                current = current[key]
            else:
                return None
        elif isinstance(current, list):
            try:
                index = int(key)
                if 0 <= index < len(current):
                    current = current[index]
                else:
                    return None
            except ValueError:
                return None
        else:
            return None
    return current
if __name__ == '__main__':
    sample_data = {'user': {'profile': {'name': 'Alice', 'age': 30}, 'settings': {'notifications': {'email': True, 'sms': False}}}, 'items': [{'id': 1, 'val': 'first'}, {'id': 2, 'val': 'second'}]}
    print(resolve_nested_value(sample_data, 'user.profile.name'))
    print(resolve_nested_value(sample_data, 'user.settings.notifications.sms'))
    print(resolve_nested_value(sample_data, 'items.1.val'))
    print(resolve_nested_value(sample_data, 'missing.key'))