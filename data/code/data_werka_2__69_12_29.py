def retrieve_nested_value(data, keys):
    try:
        value = data
        for key in keys:
            value = value[key]
        return value
    except (KeyError, TypeError) as e:
        raise ValueError('Invalid key or path') from e
if __name__ == '__main__':
    sample_data = {'a': {'b': {'c': 42, 'd': [1, 2, 3]}, 'e': 'hello'}, 'f': True}
    keys_to_retrieve = ['a', 'b', 'c']
    result = retrieve_nested_value(sample_data, keys_to_retrieve)
    print(result)