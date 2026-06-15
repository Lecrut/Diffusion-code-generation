def find_absolute_smallest(list_of_lists):
    smallest = float('inf')
    found_any = False
    for sublist in list_of_lists:
        if sublist:
            current_min = min(abs(x) for x in sublist)
            if current_min < smallest:
                smallest = current_min
            found_any = True
    if not found_any:
        return None
    return smallest
if __name__ == '__main__':
    test_case_1 = [[1, 5, -3], [10, -20]]
    test_case_2 = [[100], [-50, 10], []]
    test_case_3 = [[5], [10], [-1]]
    test_case_4 = [[100, 200], [], [-50]]
    test_case_5 = [[], [], []]
    test_case_6 = [[-10], [20], [-30]]
    print(f"Test Case 1: {find_absolute_smallest(test_case_1)}")
    print(f"Test Case 2: {find_absolute_smallest(test_case_2)}")
    print(f"Test Case 3: {find_absolute_smallest(test_case_3)}")
    print(f"Test Case 4: {find_absolute_smallest(test_case_4)}")
    print(f"Test Case 5: {find_absolute_smallest(test_case_5)}")
    print(f"Test Case 6: {find_absolute_smallest(test_case_6)}")