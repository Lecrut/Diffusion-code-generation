def retrieve_elements(data_dict, keys):
    result = {}
    for key in keys:
        if key in data_dict:
            result[key] = data_dict[key]
    return result

if __name__ == '__main__':
    sample_data = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    }
    keys_to_retrieve = ['a', 'c', 'e']
    retrieved_elements = retrieve_elements(sample_data, keys_to_retrieve)
    print(retrieved_elements)