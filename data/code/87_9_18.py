def can_proceed(is_active: bool, has_permission: bool) -> bool:
    return is_active and has_permission

if __name__ == '__main__':
    check1 = True
    check2 = False
    result1 = can_proceed(check1, check2)
    print(f"Can proceed with {check1} and {check2}: {result1}")
    check3 = True
    check4 = True
    result2 = can_proceed(check3, check4)
    print(f"Can proceed with {check3} and {check4}: {result2}")
    check5 = False
    check6 = False
    result3 = can_proceed(check5, check6)
    print(f"Can proceed with {check5} and {check6}: {result3}")