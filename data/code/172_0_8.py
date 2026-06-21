def map_int_to_str(input_dict):
    return {key: value for key, value in input_dict.items()}

if __name__ == '__main__':
    sample_dict = {1: 'one', 2: 'two', 3: 'three'}
    result = map_int_to_str(sample_dict)
    print(result)