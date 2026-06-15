def exists_set_method(element, input_list):
    set_of_list = set(input_list)
    return element in set_of_list
if __name__ == '__main__':
    target_element = 5
    data_list = [1, 3, 5, 7, 9]
    result = exists_set_method(target_element, data_list)
    print(result)
    target_element = 10
    data_list = [1, 3, 5, 7, 9]
    result = exists_set_method(target_element, data_list)
    print(result)