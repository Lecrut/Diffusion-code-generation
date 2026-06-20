def check_any_true(boolean_list):
    if not isinstance(boolean_list, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, bool) for x in boolean_list):
        raise ValueError("List must contain only boolean values")
    return any(boolean_list)

if __name__ == '__main__':
    list1 = [False, False, False, True, False]
    list2 = [False, False, False]
    list3 = [True, True, True]
    list4 = []
    list5 = [False]
    print(f"List 1: {check_any_true(list1)}")
    print(f"List 2: {check_any_true(list2)}")
    print(f"List 3: {check_any_true(list3)}")
    print(f"List 4: {check_any_true(list4)}")
    print(f"List 5: {check_any_true(list5)}")