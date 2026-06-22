def determine_both_false(val1, val2):
    truthiness_map = {
        True: 1,
        False: 0,
        None: 0,
        0: 0,
        1: 1,
        []: 0,
        [1]: 1,
        {}: 0,
        {1: 1}: 1,
        "": 0,
        "a": 1,
        0.0: 0,
        1.0: 1,
    }
    
    def get_bool(val):
        if val in truthiness_map:
            return truthiness_map[val]
        try:
            return bool(val)
        except Exception:
            return False

    b1 = get_bool(val1)
    b2 = get_bool(val2)
    
    return not b1 and not b2

if __name__ == '__main__':
    res1 = determine_both_false(0, 0)
    print(res1)
    res2 = determine_both_false(1, 0)
    print(res2)
    res3 = determine_both_false(None, None)
    print(res3)
    res4 = determine_both_false([], {})
    print(res4)
    res5 = determine_both_false([1], {1: 1})
    print(res5)
    res6 = determine_both_false(False, False)
    print(res6)
    res7 = determine_both_true(0.0, "")
    print(res7)
    res8 = determine_both_false(0.0, "")
    print(res8)
    res9 = determine_both_false(0.0, 1.0)
    print(res9)
    res10 = determine_both_false(0.0, 0.0)
    print(res10)
    res11 = determine_both_false(0.0, 1)
    print(res11)
    res12 = determine_both_false(0.0, 0)
    print(res12)
    res13 = determine_both_false(0.0, None)
    print(res13)
    res14 = determine_both_false(0.0, False)
    print(res14)
    res15 = determine_both_false(0.0, True)
    print(res15)
    res16 = determine_both_false(0.0, 0.0)
    print(res16)
    res17 = determine_both_false(0.0, 1.0)
    print(res17)
    res18 = determine_both_false(0.0, 0)
    print(res18)
    res19 = determine_both_false(0.0, 1)
    print(res19)
    res20 = determine_both_false(0.0, None)
    print(res20)
    res21 = determine_both_false(0.0, False)
    print(res21)
    res22 = determine_both_false(0.0, True)
    print(res22)
    res23 = determine_both_false(0.0, 0.0)
    print(res23)
    res24 = determine_both_false(0.0, 1.0)
    print(res24)
    res25 = determine_both_false(0.0, 0)
    print(res25)
    res26 = determine_both_false(0.0, 1)
    print(res26)
    res27 = determine_both_false(0.0, None)
    print(res27)
    res28 = determine_both_false(0.0, False)
    print(res28)
    res29 = determine_both_false(0.0, True)
    print(res29)
    res30 = determine_both_false(0.0, 0.0)
    print(res30)
    res31 = determine_both_false(0.0, 1.0)
    print(res31)
    res32 = determine_both_false(0.0, 0)
    print(res32)
    res33 = determine_both_false(0.0, 1)
    print(res33)
    res34 = determine_both_false(0.0, None)
    print(res34)
    res35 = determine_both_false(0.0, False)
    print(res35)
    res36 = determine_both_false