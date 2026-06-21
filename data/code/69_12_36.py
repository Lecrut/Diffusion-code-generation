def retrieve_nested_value(data, keys):
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current
if __name__ == '__main__':
    sample_data = {'user': {'id': 123, 'profile': {'name': 'John Doe', 'email': 'john.doe@example.com'}, 'preferences': {'theme': 'dark', 'notifications': True}}}
    keys_to_retrieve = ['user', 'profile', 'name']
    result = retrieve_nested_value(sample_data, keys_to_retrieve)
    print(result)
    invalid_keys = ['user', 'settings', 'language']
    invalid_result = retrieve_nested_value(sample_data, invalid_keys)
    print(invalid_result)