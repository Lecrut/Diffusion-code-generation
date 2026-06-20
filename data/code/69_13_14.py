def retrieve_nested_elements(data_dict, keys):
    return [data_dict[key] for key in keys if key in data_dict]
if __name__ == '__main__':
    sample_data = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}, 'g': {'h': 5, 'i': 6}}
    keys_to_retrieve = ['b', 'f', 'x']
    result = retrieve_nested_elements(sample_data, keys_to_retrieve)
    print(result)