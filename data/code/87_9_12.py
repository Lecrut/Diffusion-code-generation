def can_proceed(is_active: bool, has_permission: bool) -> bool:
    return is_active and has_permission

if __name__ == '__main__':
    check1 = True
    check2 = False
    result1 = can_proceed(check1, check2)
    print(f"Can proceed (check1={check1}, check2={check2}): {result1}")
    
    check3 = True
    check4 = True
    result2 = can_proceed(check3, check4)
    print(f"Can proceed (check3={check3}, check4={check4}): {result2}")
    
    check5 = False
    check6 = False
    result3 = can_proceed(check5, check6)
    print(f"Can proceed (check5={check5}, check6={check6}): {result3}")