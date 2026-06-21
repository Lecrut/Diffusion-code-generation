def map_keys_to_values(keys):
    key_value_map = {'a': 1, 'b': 2, 'c': 3}
    return [key_value_map.get(key, 0) for key in keys]
if __name__ == '__main__':
    sample_keys = ['a', 'b', 'd', 'e']
    print(map_keys_to_values(sample_keys))