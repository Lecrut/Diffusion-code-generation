def retrieve_nested_value(data, keys):
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list) and isinstance(key, int) and (0 <= key < len(current)):
            current = current[key]
        else:
            raise ValueError('Invalid keys or data structure')
    return current
if __name__ == '__main__':
    sample_data = {'a': {'b': {'c': 42, 'd': 'hello'}, 'e': [1, 2, 3]}, 'f': True, 'g': [{'h': 1}, {'i': 2}]}
    keys_to_retrieve_1 = ['a', 'b', 'c']
    result_1 = retrieve_nested_value(sample_data, keys_to_retrieve_1)
    print(result_1)
    keys_to_retrieve_2 = ['a', 'e', 1]
    result_2 = retrieve_nested_value(sample_data, keys_to_retrieve_2)
    print(result_2)
    keys_to_retrieve_3 = ['g', 1, 'i']
    result_3 = retrieve_nested_value(sample_data, keys_to_retrieve_3)
    print(result_3)