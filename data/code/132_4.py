def check_all_true(bool_list):
    for item in bool_list:
        if not item:
            return False
    return True
if __name__ == '__main__':
    list1 = [True, True, True]
    list2 = [True, False, True]
    list3 = [True, True]
    list4 = []
    list5 = [False]
    list6 = [True, True, False, True]
    print(f"list1: {check_all_true(list1)}")
    print(f"list2: {check_all_true(list2)}")
    print(f"list3: {check_all_true(list3)}")
    print(f"list4: {check_all_true(list4)}")
    print(f"list5: {check_all_true(list5)}")
    print(f"list6: {check_all_true(list6)}")