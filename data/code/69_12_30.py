def retrieve_nested_value(data, keys):
    try:
        value = data
        for key in keys:
            if isinstance(value, dict):
                value = value[key]
            elif isinstance(value, list) and isinstance(key, int):
                value = value[key]
            else:
                raise ValueError('Invalid keys or data structure')
        return value
    except (KeyError, IndexError, TypeError):
        raise ValueError('Invalid keys or data structure')
if __name__ == '__main__':
    sample_data = {'a': {'b': {'c': 42, 'd': 'hello'}, 'e': [1, 2, 3]}, 'f': True, 'g': [{'h': 99}, {'i': 100}]}
    keys_to_retrieve = ['a', 'b', 'c']
    print(retrieve_nested_value(sample_data, keys_to_retrieve))
    keys_to_retrieve = ['a', 'e', 1]
    print(retrieve_nested_value(sample_data, keys_to_retrieve))
    keys_to_retrieve = ['f']
    print(retrieve_nested_value(sample_data, keys_to_retrieve))
    keys_to_retrieve = ['g', 0, 'h']
    print(retrieve_nested_value(sample_data, keys_to_retrieve))
    keys_to_retrieve = ['a', 'b', 'z']
    try:
        print(retrieve_nested_value(sample_data, keys_to_retrieve))
    except ValueError as e:
        print(e)