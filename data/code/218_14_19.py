def flatten_and_find_min(nested_list):
    if not nested_list:
        raise ValueError("Input list is empty")
    
    flattened = []
    for sublist in nested_list:
        if sublist:
            flattened.extend(sublist)
    
    if not flattened:
        raise ValueError("All sublists are empty")
    
    return min(flattened)

if __name__ == '__main__':
    test_case_1 = [[1, 5, 3], [8, 2, 9]]
    test_case_2 = [[10, 20], [5, 15]]
    test_case_3 = []
    test_case_4 = [[]]
    test_case_5 = [[-5], [100], [-1]]
    
    print(f"Test Case 1: {test_case_1} -> Minimum: {flatten_and_find_min(test_case_1)}")
    print(f"Test Case 2: {test_case_2} -> Minimum: {flatten_and_find_min(test_case_2)}")
    try:
        print(f"Test Case 3: {test_case_3} -> Minimum: {flatten_and_find_min(test_case_3)}")
    except ValueError as e:
        print(e)
    
    try:
        print(f"Test Case 4: {test_case_4} -> Minimum: {flatten_and_find_min(test_case_4)}")
    except ValueError as e:
        print(e)
    
    print(f"Test Case 5: {test_case_5} -> Minimum: {flatten_and_find_min(test_case_5)}")