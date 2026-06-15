def find_minimum_in_list_of_lists(list_of_lists):
    if not list_of_lists:
        raise ValueError("Input list of lists is empty")
    all_elements = []
    for sublist in list_of_lists:
        if sublist:
            all_elements.extend(sublist)
    if not all_elements:
        raise ValueError("All sublists are empty")
    return min(all_elements)
if __name__ == '__main__':
    test_case_1 = [[1, 5, 3], [8, 2, 9]]
    test_case_2 = [[10, 20], [5, 15]]
    test_case_3 = []
    test_case_4 = [[]]
    test_case_5 = [[-5], [10], [-1]]
    print(f"Test Case 1: {test_case_1} -> Minimum: {find_minimum_in_list_of_lists(test_case_1)}")
    print(f"Test Case 2: {test_case_2} -> Minimum: {find_minimum_in_list_of_lists(test_case_2)}")
    print(f"Test Case 3: {test_case_3} -> Error: ", end="")
    try:
        find_minimum_in_list_of_lists(test_case_3)
    except ValueError as e:
        print(e)
    print(f"Test Case 4: {test_case_4} -> Error: ", end="")
    try:
        find_minimum_in_list_of_lists(test_case_4)
    except ValueError as e:
        print(e)
    print(f"Test Case 5: {test_case_5} -> Minimum: {find_minimum_in_list_of_lists(test_case_5)}")