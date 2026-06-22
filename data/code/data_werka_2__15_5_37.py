def compare_keys(input_dict, key1, key2):
    return {key1: input_dict.get(key1) == input_dict.get(key2)}

if __name__ == '__main__':
    sample_dict = {'first': 30, 'second': 45, 'third': 30}
    key_to_compare = 'first'
    another_key_to_compare = 'third'
    
    comparison_result = compare_keys(sample_dict, key_to_compare, another_key_to_compare)
    print(comparison_result)