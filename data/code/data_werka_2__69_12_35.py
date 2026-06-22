def retrieve_nested_value(nested_dict, keys):
    try:
        value = nested_dict
        for key in keys:
            value = value[key]
        return value
    except KeyError as e:
        raise ValueError(f'Key not found: {e}')
if __name__ == '__main__':
    sample_data = {'a': {'b': {'c': 42, 'd': 99}, 'e': 3.14}, 'f': [1, 2, 3]}
    keys_to_retrieve = ['a', 'b', 'c']
    result = retrieve_nested_value(sample_data, keys_to_retrieve)
    print(result)