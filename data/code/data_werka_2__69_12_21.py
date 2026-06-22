def retrieve_nested_value(data, keys):
    try:
        value = data
        for key in keys:
            value = value[key]
        return value
    except (KeyError, TypeError):
        raise ValueError('Invalid keys or data structure')
if __name__ == '__main__':
    sample_data = {'a': {'b': {'c': 42, 'd': 'hello'}, 'e': [1, 2, 3]}, 'f': True}
    keys_to_retrieve = ['a', 'b', 'c']
    result = retrieve_nested_value(sample_data, keys_to_retrieve)
    print(result)
    keys_to_retrieve = ['a', 'e', 1]
    result = retrieve_nested_value(sample_data, keys_to_retrieve)
    print(result)