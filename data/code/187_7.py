def find_largest_robust(list1, list2, list3):
    all_lists = [list1, list2, list3]
    largest = -float('inf')
    for lst in all_lists:
        if not lst:
            continue
        current_max = max(lst)
        if current_max > largest:
            largest = current_max
    return largest
if __name__ == '__main__':
    test_case_1_list1 = [-10, -5, 0]
    test_case_2_list2 = [1, 5, 100]
    test_case_3_list3 = [-200, 42, 99]
    result1 = find_largest_robust(test_case_1_list1, test_case_2_list2, test_case_3_list3)
    print(f"Test Case 1: {result1}")
    test_case_4_list1 = [-50, -100]
    test_case_5_list2 = [0]
    test_case_6_list3 = [-1, -2]
    result2 = find_largest_robust(test_case_4_list1, test_case_5_list2, test_case_6_list3)
    print(f"Test Case 2: {result2}")
    test_case_7_list1 = [10]
    test_case_8_list2 = [-5, -10]
    test_case_9_list3 = [0, 5]
    result3 = find_largest_robust(test_case_7_list1, test_case_8_list2, test_case_9_list3)
    print(f"Test Case 3: {result3}")
    test_case_10_list1 = []
    test_case_11_list2 = [5]
    test_case_12_list3 = [-5]
    result4 = find_largest_robust(test_case_10_list1, test_case_11_list2, test_case_12_list3)
    print(f"Test Case 4: {result4}")