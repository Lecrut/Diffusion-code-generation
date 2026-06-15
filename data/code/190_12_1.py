def exists_set_method(element, data_list):
    data_set = set(data_list)
    return element in data_set
if __name__ == '__main__':
    target_element = 5
    sample_list = [1, 3, 5, 7, 9]
    result = exists_set_method(target_element, sample_list)
    print(result)
    target_element = 10
    sample_list = [1, 3, 5, 7, 9]
    result = exists_set_method(target_element, sample_list)
    print(result)