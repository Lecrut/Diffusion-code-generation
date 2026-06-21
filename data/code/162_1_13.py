def map_keys_to_values(keys):
    mapping = {'apple': 1, 'banana': 2, 'cherry': 3}
    return [mapping.get(key, 0) for key in keys]
if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'orange', 'cherry']
    print(map_keys_to_values(sample_keys))