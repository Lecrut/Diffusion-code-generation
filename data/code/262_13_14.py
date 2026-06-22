def find_min_max_keys(input_dict):
    min_key = min(input_dict, key=input_dict.get)
    max_key = max(input_dict, key=input_dict.get)
    return (min_key, max_key)

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 2}
    result = find_min_max_keys(sample_dict)
    print(result)