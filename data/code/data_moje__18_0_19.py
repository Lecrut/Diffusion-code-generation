def find_middle_element(data):
    length = len(data)
    if length == 0:
        return None
    middle_index = length // 2
    return data[middle_index]

if __name__ == '__main__':
    test_cases_odd = [1, 3, 5, 7, 9]
    test_cases_even = [10, 20, 30, 40]
    test_cases_empty = []
    
    result_odd = find_middle_element(test_cases_odd)
    result_even = find_middle_element(test_cases_even)
    result_empty = find_middle_element(test_cases_empty)
    
    print(result_odd)
    print(result_even)
    print(result_empty)