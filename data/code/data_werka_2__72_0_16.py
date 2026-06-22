def compare_elements(list1, list2, index):
    if not isinstance(list1, (list, tuple)):
        raise ValueError("list1 must be a list or tuple")
    if not isinstance(list2, (list, tuple)):
        raise ValueError("list2 must be a list or tuple")
    if not isinstance(index, int):
        raise ValueError("index must be an integer")
    
    length1 = len(list1)
    length2 = len(list2)
    
    if index < 0:
        adjusted_index1 = length1 + index
        adjusted_index2 = length2 + index
    else:
        adjusted_index1 = index
        adjusted_index2 = index
        
    element1 = None
    element2 = None
    
    if 0 <= adjusted_index1 < length1:
        element1 = list1[adjusted_index1]
        
    if 0 <= adjusted_index2 < length2:
        element2 = list2[adjusted_index2]
        
    return element1, element2

if __name__ == '__main__':
    sample_list_a = [10, 20, 30, 40]
    sample_list_b = [11, 22, 33, 44]
    valid_index = 2
    invalid_index = 10
    
    result_valid = compare_elements(sample_list_a, sample_list_b, valid_index)
    print(result_valid)
    
    result_invalid = compare_elements(sample_list_a, sample_list_b, invalid_index)
    print(result_invalid)
    
    result_negative = compare_elements(sample_list_a, sample_list_b, -1)
    print(result_negative)