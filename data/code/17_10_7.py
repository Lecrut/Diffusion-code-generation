def get_last_element(items):
    if not items:
        return None
    return items[-1]

if __name__ == '__main__':
    test_list_1 = [10, 20, 30, 40]
    test_list_2 = []
    test_list_3 = ['apple', 'banana', 'cherry']
    
    result_1 = get_last_element(test_list_1)
    result_2 = get_last_element(test_list_2)
    result_3 = get_last_element(test_list_3)
    
    print(result_1)
    print(result_2)
    print(result_3)