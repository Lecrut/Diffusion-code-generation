def check_any_true(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    
    count_true = 0
    for item in values:
        if item is True:
            return True
        if not isinstance(item, bool):
            raise ValueError("All elements must be boolean")
            
    return False

if __name__ == '__main__':
    test_list = [False, False, False, False]
    answer = check_any_true(test_list)
    print(answer)
    
    test_list_2 = [False, True, False]
    answer_2 = check_any_true(test_list_2)
    print(answer_2)
    
    test_list_3 = []
    answer_3 = check_any_true(test_list_3)
    print(answer_3)