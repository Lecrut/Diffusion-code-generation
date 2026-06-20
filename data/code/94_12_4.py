def check_any_true(lst):
    return any(lst)

if __name__ == '__main__':
    test_list1 = [False, False, False]
    test_list2 = [False, True, False]
    test_list3 = [True, False, False]
    test_list4 = []
    test_list5 = [False]

    print(f"List 1: {test_list1}, Result: {check_any_true(test_list1)}")
    print(f"List 2: {test_list2}, Result: {check_any_true(test_list2)}")
    print(f"List 3: {test_list3}, Result: {check_any_true(test_list3)}")
    print(f"List 4: {test_list4}, Result: {check_any_true(test_list4)}")
    print(f"List 5: {test_list5}, Result: {check_any_true(test_list5)}")