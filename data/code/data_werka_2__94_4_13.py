def check_existence(data_list):
    if not isinstance(data_list, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    
    flag_present = False
    true_found = False
    
    index = 0
    length = len(data_list)
    
    while index < length:
        current_val = data_list[index]
        if not isinstance(current_val, bool):
            raise ValueError("All elements must be boolean")
        
        if current_val is True:
            true_found = True
            flag_present = True
            break
        
        index += 1
        
    return true_found

if __name__ == '__main__':
    sample_flags_1 = [False, False, False, False]
    sample_flags_2 = [False, False, True, False]
    sample_flags_3 = []
    sample_flags_4 = [True, True, True]
    sample_flags_5 = [False]
    
    result_1 = check_existence(sample_flags_1)
    result_2 = check_existence(sample_flags_2)
    result_3 = check_existence(sample_flags_3)
    result_4 = check_existence(sample_flags_4)
    result_5 = check_existence(sample_flags_5)
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)