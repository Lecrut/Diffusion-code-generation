def map_dict_to_strings(input_dict):
    return {key: str(value) for key, value in input_dict.items()}

if __name__ == '__main__':
    sample_dict = {1: 10, 2: 20, 3: 30}
    result = map_dict_to_strings(sample_dict)
    print(result)