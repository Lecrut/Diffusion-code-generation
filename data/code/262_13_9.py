def find_min_max_keys(input_dict):
    if not input_dict:
        return None, None
    min_key = max_key = list(input_dict.keys())[0]
    for key in input_dict:
        if input_dict[key] < input_dict[min_key]:
            min_key = key
        elif input_dict[key] > input_dict[max_key]:
            max_key = key
    return min_key, max_key

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 3}
    print(find_min_max_keys(sample_dict))