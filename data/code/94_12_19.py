def check_any_true(boolean_list):
    if not boolean_list:
        return False
    return any(boolean_list)

if __name__ == '__main__':
    list1 = [False, False, False]
    list2 = [False, True, False]
    list3 = [True, True, False]
    list4 = []
    list5 = [False]
    print(f"List 1: {list1}, Result: {check_any_true(list1)}")
    print(f"List 2: {list2}, Result: {check_any_true(list2)}")
    print(f"List 3: {list3}, Result: {check_any_true(list3)}")
    print(f"List 4: {list4}, Result: {check_any_true(list4)}")
    print(f"List 5: {list5}, Result: {check_any_true(list5)}")