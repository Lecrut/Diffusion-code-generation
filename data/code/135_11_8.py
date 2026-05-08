def check_equivalence(expr1, expr2):
    if isinstance(expr1, bool) and isinstance(expr2, bool):
        return expr1 == expr2
    if isinstance(expr1, list) and isinstance(expr2, list):
        if len(expr1) != len(expr2):
            return False
        for b1, b2 in zip(expr1, expr2):
            if b1 != b2:
                return False
        return True
    return False
if __name__ == '__main__':
    print(f"Test 1 (True vs True): {check_equivalence(True, True)}")
    print(f"Test 2 (False vs False): {check_equivalence(False, False)}")
    print(f"Test 3 (True vs False): {check_equivalence(True, False)}")
    list1 = [True, False, True]
    list2 = [True, False, True]
    print(f"Test 4 (List equal): {check_equivalence(list1, list2)}")
    list3 = [True, False, True]
    list4 = [False, True, True]
    print(f"Test 5 (List unequal): {check_equivalence(list3, list4)}")
    list5 = [True, True]
    list6 = [True, False]
    print(f"Test 6 (List unequal length): {check_equivalence(list5, list6)}")
    list7 = [True]
    list8 = [True]
    print(f"Test 7 (Single element equal): {check_equivalence(list7, list8)}")
    list9 = [True, True, True]
    list10 = [True, True]
    print(f"Test 8 (List unequal length): {check_equivalence(list9, list10)}")