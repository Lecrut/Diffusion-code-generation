def safe_second_element(lst):
    return lst[1] if len(lst) > 1 else None

if __name__ == '__main__':
    sample_list_1 = [100, 200, 300]
    sample_list_2 = [400]
    sample_list_3 = []
    
    test_cases = {
        'list_with_two_elements': sample_list_1,
        'list_with_one_element': sample_list_2,
        'empty_list': sample_list_3
    }
    
    for description, lst in test_cases.items():
        print(f"{description}: {safe_second_element(lst)}")