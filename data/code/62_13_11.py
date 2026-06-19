def safe_second_element(lst):
    if len(lst) < 2:
        return None
    return lst[1]

if __name__ == '__main__':
    sample_list_1 = [5, 15, 25]
    sample_list_2 = ['x']
    sample_list_3 = []
    
    result_1 = safe_second_element(sample_list_1)
    result_2 = safe_second_element(sample_list_2)
    result_3 = safe_second_element(sample_list_3)
    
    print(result_1)
    print(result_2)
    print(result_3)