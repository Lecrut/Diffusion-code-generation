def retrieve_nested_value(data, keys):
    try:
        for key in keys:
            data = data[key]
        return data
    except KeyError:
        raise ValueError('Key not found in the nested dictionary')
if __name__ == '__main__':
    sample_data = {'a': {'b': {'c': 42, 'd': 99}, 'e': 100}, 'f': 200}
    keys_to_retrieve = ['a', 'b', 'c']
    result = retrieve_nested_value(sample_data, keys_to_retrieve)
    print(result)