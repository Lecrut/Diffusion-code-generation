def retrieve_nested_value(data, keys):
    try:
        value = data
        for key in keys:
            value = value[key]
        return value
    except (KeyError, TypeError):
        raise ValueError('Invalid keys or data structure')
if __name__ == '__main__':
    sample_data = {'a': {'b': {'c': 42, 'd': 100}, 'e': 300}, 'f': {'g': 500}}
    keys_to_retrieve = ['a', 'b', 'c']
    result = retrieve_nested_value(sample_data, keys_to_retrieve)
    print(result)
    keys_to_retrieve = ['f', 'g']
    result = retrieve_nested_value(sample_data, keys_to_retrieve)
    print(result)
    keys_to_retrieve = ['a', 'b', 'z']
    try:
        result = retrieve_nested_value(sample_data, keys_to_retrieve)
        print(result)
    except ValueError as e:
        print(e)