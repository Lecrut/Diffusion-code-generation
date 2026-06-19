def access_elements():
    tuple_data = (100, 200, 300, 400, 500)
    dict_data = {'x': [10, 20, 30], 'y': [40, 50, 60], 'z': [70, 80, 90]}
    
    last_element_tuple = tuple_data[-1]
    second_to_last_value_dict = dict_data['y'][-2]
    
    return last_element_tuple, second_to_last_value_dict

if __name__ == '__main__':
    result = access_elements()
    print(result)