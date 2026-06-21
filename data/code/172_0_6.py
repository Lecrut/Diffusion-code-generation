def map_integers_to_strings(input_dict):
    return {key: value for key, value in input_dict.items()}

if __name__ == '__main__':
    sample_dict = {1: 'one', 2: 'two', 3: 'three'}
    result = map_integers_to_strings(sample_dict)
    print(result)