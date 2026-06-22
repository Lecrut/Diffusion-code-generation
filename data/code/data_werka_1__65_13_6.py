def validate_tuple(sample_tuple):
    if not isinstance(sample_tuple, tuple) or len(sample_tuple) == 0:
        raise ValueError("Invalid sample tuple")

def validate_dict_values(sample_dict):
    if not isinstance(sample_dict, dict) or len(sample_dict.values()) < 2:
        raise ValueError("Invalid sample dictionary")
    for values_list in sample_dict.values():
        if not isinstance(values_list, list) or len(values_list) < 2:
            raise ValueError("Values list in dictionary is invalid")

def access_elements():
    sample_tuple = (10, 20, 30, 40, 50)
    sample_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    
    validate_tuple(sample_tuple)
    validate_dict_values(sample_dict)
    
    last_element_tuple = sample_tuple[-1]
    second_to_last_value_dict = next(iter(sample_dict.values()))[-2]
    
    return last_element_tuple, second_to_last_value_dict

if __name__ == '__main__':
    result = access_elements()
    print(result)