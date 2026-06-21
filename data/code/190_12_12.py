def exists_set_method(element, data_list):
    return element in set(data_list)

if __name__ == '__main__':
    target_element = 5
    sample_list = [1, 3, 5, 7, 9]
    result = exists_set_method(target_element, sample_list)
    print(f"Does {target_element} exist in {sample_list}? {result}")
    
    target_element = 10
    sample_list = [1, 3, 5, 7, 9]
    result = exists_set_method(target_element, sample_list)
    print(f"Does {target_element} exist in {sample_list}? {result}")
    
    target_element = 5
    sample_list = [5, 10, 15]
    result = exists_set_method(target_element, sample_list)
    print(f"Does {target_element} exist in {sample_list}? {result}")