def access_elements():
    sample_tuple = (10, 20, 30, 40, 50)
    sample_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    
    last_element_tuple = sample_tuple[-1]
    second_to_last_value_dict = list(sample_dict.values())[1][-2]
    
    return last_element_tuple, second_to_last_value_dict

if __name__ == '__main__':
    result = access_elements()
    print(result)