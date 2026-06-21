def map_dict_to_list(input_dict):
    return {key: value for key, value in input_dict.items()}

if __name__ == '__main__':
    sample_dict = {1: 'one', 2: 'two', 3: 'three'}
    result = map_dict_to_list(sample_dict)
    print(result)