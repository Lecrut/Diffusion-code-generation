def check_any_true(boolean_list):
    for value in boolean_list:
        if value:
            return True
    return False
if __name__ == '__main__':
    list1 = [False, False, False, True, False]
    list2 = [False, False, False]
    list3 = [True, True, True]
    list4 = []
    print(f"List 1: {list1}, Result: {check_any_true(list1)}")
    print(f"List 2: {list2}, Result: {check_any_true(list2)}")
    print(f"List 3: {list3}, Result: {check_any_true(list3)}")
    print(f"List 4: {list4}, Result: {check_any_true(list4)}")