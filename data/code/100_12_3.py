def check_all_same(bool_list):
    if not bool_list:
        return True
    first_value = bool_list[0]
    return all(x == first_value for x in bool_list)
if __name__ == '__main__':
    list1 = [True, True, True]
    list2 = [False, False, False]
    list3 = [True, False, True]
    list4 = [False, False, True]
    list5 = []
    list6 = [True]
    print(f"List 1: {list1}, Result: {check_all_same(list1)}")
    print(f"List 2: {list2}, Result: {check_all_same(list2)}")
    print(f"List 3: {list3}, Result: {check_all_same(list3)}")
    print(f"List 4: {list4}, Result: {check_all_same(list4)}")
    print(f"List 5: {list5}, Result: {check_all_same(list5)}")
    print(f"List 6: {list6}, Result: {check_all_same(list6)}")