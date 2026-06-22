def access_elements():
    sample_tuple = (10, 20, 30, 40, 50)
    sample_dict = {'x': [1, 2, 3], 'y': [4, 5, 6], 'z': [7, 8, 9]}
    
    def get_last_element(tpl):
        return tpl[-1]
    
    def get_second_to_last_value(dct):
        keys = list(dct.keys())
        if len(keys) < 2:
            raise ValueError("Dictionary does not have enough keys")
        second_key = keys[1]
        values_list = dct[second_key]
        if len(values_list) < 2:
            raise ValueError("Values list is too short")
        return values_list[-2]
    
    last_element_tuple = get_last_element(sample_tuple)
    second_to_last_value_dict = get_second_to_last_value(sample_dict)
    
    return (last_element_tuple, second_to_last_value_dict)

if __name__ == '__main__':
    result = access_elements()
    print(result)