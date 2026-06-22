def retrieve_nested_value(data, keys):
    try:
        result = data
        for key in keys:
            result = result[key]
        return result
    except (KeyError, TypeError):
        raise ValueError('Invalid key sequence or data structure')
if __name__ == '__main__':
    sample_data = {'a': {'b': {'c': 42, 'd': 'hello'}, 'e': [1, 2, 3]}, 'f': True}
    keys_to_retrieve = ['a', 'b', 'c']
    print(retrieve_nested_value(sample_data, keys_to_retrieve))
    keys_to_retrieve = ['a', 'e', 1]
    print(retrieve_nested_value(sample_data, keys_to_retrieve))
    keys_to_retrieve = ['f']
    print(retrieve_nested_value(sample_data, keys_to_retrieve))