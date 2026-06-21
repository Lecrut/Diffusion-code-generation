def map_int_to_str(input_dict):
    return {k: v for k, v in input_dict.items() if isinstance(v, str)}

if __name__ == '__main__':
    sample_dict = {1: 'one', 2: 'two', 3: 3, 4: 'four'}
    result = map_int_to_str(sample_dict)
    print(result)